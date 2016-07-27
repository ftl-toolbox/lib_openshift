from __future__ import absolute_import
import os
import yaml
import json
import importlib
import time
from .api_client import ApiClient
from .rest import ApiException
from .models import V1ObjectMeta,V1DeleteOptions
from .apis import ApiV1,OapiV1


class WrapperException(Exception):

    def __init__(self, msg, **kwargs):
        self.msg = msg
        self.value = kwargs
        self.value['msg'] = msg

    def __str__(self):
        return json.dumps(self.value)


class Wrapper(object):

    def _validate_common_args(self, namespaced=True, namespace=None,
                              name=None, labels=None,
                              annotations=None, state='present'):
        # TODO: validate name against k8s limitations
        if name is None:
            raise WrapperException(msg="name is required")

        if namespaced and namespace is None:
            raise WrapperException(msg="namespace is required")

        if state not in ('present', 'absent'):
            raise WrapperException(msg="Unknown state: {0}".format(state))

        if labels is not None and not is_instance(dict, labels):
            raise WrapperException(msg="labels must be a dict")

        if annotations is not None and not is_instance(dict, annotations):
            raise WrapperException(msg="annotations must be a dict")


    def _get_crud_ops(self, model):
        operations = model.operations
        namespaced_ops = [op for op in operations if op['namespaced']]
        non_namespaced_ops = [op for op in operations if not op['namespaced']]

        crud_ops = {}
        for op_type in ('create', 'read', 'update', 'delete'):
            for op in namespaced_ops:
                if op_type == op['type']:
                    crud_ops[op_type] = op
            for op in non_namespaced_ops:
                if op_type not in crud_ops and op_type == op['type']:
                    crud_ops[op_type] = op
        return crud_ops


    def _get_api(self, api_class):
        # TODO: add basic auth, client cert auth, ca certificate and
        # tls_insecure settings
        header_name = None
        header_value = None
        if 'token' in self._user:
            header_name = 'Authorization'
            header_value = 'Bearer {0}'.format(self._user['token'])
        api_client = ApiClient(host=self._cluster['server'],
                               header_name=header_name,
                               header_value=header_value)
        api = api_class(api_client=api_client)
        return api

    def _get_k8s_object(self, api, method, name, namespace):
        k8s_object = None

        try:
            if namespace is None:
                k8s_object = getattr(api, method)(name)
            else:
                k8s_object = getattr(api, method)(namespace, name)
            already_exists = True
        except ApiException as e:
            if e.status != 404:
                raise WrapperException(msg="api request failed code: {0}, reason: {1}".format(e.status, e.reason))

        return k8s_object

    def _create_or_update_k8s_object(self, api, create_method,
                                     update_method, k8s_object,
                                     body, namespace):
        changed = False
        result = {}

        if k8s_object is not None:
            # TODO: compare k8s_object and body, update if needed
            changed = False
            result = k8s_object
        else:
            try:
                if namespace is None:
                    k8s_object = getattr(api, create_method)(body)
                else:
                    k8s_object = getattr(api, create_method)(body, namespace)
                changed = True
                result = k8s_object.to_dict()
            except ApiException as e:
                raise WrapperException(msg="api request failed code: {0}, reason: {1}".format(e.status, e.reason))
        return (changed, result)

    def _delete_k8s_object(self, api, delete_method, k8s_object,
                           delete_options, name, namespace):
        changed = False
        status = {}
        if k8s_object is not None:
            try:
                if namespace is None:
                    status = getattr(api, delete_method)(delete_options, name)
                else:
                    status = getattr(api, delete_method)(delete_options,
                                     namespace, name)
                changed = True
            except ApiException as e:
                raise WrapperException(msg="api request failed code: {0}, reason: {1}".format(e.status, e.reason))
        return (changed, status)


    def _k8s_object(self, api_class, model, namespace, name, api_version,
                    labels, annotations, state, **model_kwargs):

        friendly_name = model.__name__.replace(api_version.capitalize(), '')

        crud_ops = self._get_crud_ops(model)

        api = self._get_api(api_class)

        k8s_object = self._get_k8s_object(api, crud_ops['read']['method'], name, namespace)

        # TODO: add check mode
        if state == 'present':
            if namespace is not None:
                self.namespace(name=namespace, api_version=api_version, state='present')
            metadata = Wrapper.metadata_from_datastructure(api_version, name=name,
                                                           labels=labels, annotations=annotations)
            body = model(kind=friendly_name, api_version=api_version,
                         metadata=metadata, **model_kwargs)
            (changed, result) = self._create_or_update_k8s_object(api,
                                                                  crud_ops['create']['method'],
                                                                  crud_ops['update']['method'],
                                                                  k8s_object,
                                                                  body, namespace)

        elif state == 'absent':
            delete_options = V1DeleteOptions()
            (changed, result) = self._delete_k8s_object(api,
                                                        crud_ops['delete']['method'],
                                                        k8s_object, delete_options,
                                                        name, namespace)

        # TODO: implement proper wait on object creation
        time.sleep(1)
        return {'changed': changed, friendly_name.lower(): result}



    def namespace(self, name=None, api_version='v1', labels=None,
                  annotations=None, state='present'):
        self._validate_common_args(False, None, name, labels, annotations, state)
        if api_version == 'v1':
            # TODO: use api derived from model operations using importlib
            #       http://stackoverflow.com/questions/13598035/importing-a-module-when-the-module-name-is-in-a-variable
            from .models import V1Namespace
            model = V1Namespace
            from .apis import ApiV1
            api_class = ApiV1
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))


        return self._k8s_object(api_class, model, None, name, api_version,
                                labels, annotations, state)


    def pod(self, namespace=None, name=None, api_version='v1', labels=None,
            annotations=None, state='present', restart_policy=None,
            node_selector=None, host_network=False, volumes=None,
            containers=None):
        self._validate_common_args(True, namespace, name, labels, annotations, state)
        if api_version == 'v1':
            from .models import V1Pod
            model = V1Pod
            from .apis import ApiV1
            api_class = ApiV1
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        pod_spec = Wrapper.pod_spec_from_datastructure(api_version,
                                                       restart_policy=restart_policy,
                                                       node_selector=node_selector,
                                                       host_network=host_network,
                                                       containers=containers)

        return self._k8s_object(api_class, model, namespace, name, api_version,
                                labels, annotations, state, spec=pod_spec)

    @staticmethod
    def pod_spec_from_datastructure(api_version, **kwargs):
        if api_version == 'v1':
            from .models import V1PodSpec, V1Container
            pod_spec_model = V1PodSpec
            container_model = V1Container
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        containers = kwargs.get('containers', [])
        if containers is None:
            containers = []
        container_objects = []
        for cd in containers:
            container_objects.append(container_model(**cd))
        kwargs['containers'] = container_objects

        pod_spec = pod_spec_model(**kwargs)
        return pod_spec

    @staticmethod
    def metadata_from_datastructure(api_version, **kwargs):
        if api_version == 'v1':
            from .models import V1ObjectMeta
            metadata_model = V1ObjectMeta
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        metadata = metadata_model(**kwargs)
        return metadata

    @staticmethod
    def pod_template_spec_from_datastructure(api_version, **kwargs):
        if api_version == 'v1':
            from .models import V1PodTemplateSpec
            pod_template_spec_model = V1PodTemplateSpec
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        metadata = Wrapper.metadata_from_datastructure(api_version, **(kwargs.get('metdata', {})))
        pod_spec = Wrapper.pod_spec_from_datastructure(api_version, **(kwargs.get('spec', {})))
        pod_template_spec = pod_template_spec_model(metadata=metadata, spec=pod_spec)
        return pod_template_spec


    def replication_controller(self, namespace=None, name=None, api_version='v1', labels=None,
                               annotations=None, state='present', replicas=1,
                               selector=None, template=None):
        self._validate_common_args(True, namespace, name, labels, annotations, state)
        if api_version == 'v1':
            from .models import V1ReplicationController, V1ReplicationControllerSpec
            model = V1ReplicationController
            rc_spec_model = V1ReplicationControllerSpec
            from .apis import ApiV1
            api_class = ApiV1
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        pod_template_spec = Wrapper.pod_template_spec_from_datastructure(api_version, **template)
        rc_spec = rc_spec_model(replicas=replicas, selector=selector,
                                template=pod_template_spec)
        print(rc_spec)

        return self._k8s_object(api_class, model, namespace, name, api_version,
                                labels, annotations, state, spec=rc_spec)



    def __init__(self, kubeconfig=None, api_endpoint=None, namespace=None,
                 username=None, password=None, token=None, client_cert=None,
                 client_key=None, certificate_authority=None,
                 certificate_authority_data = None,
                 insecure_skip_tls_verify=None):

        client_config = None

        try:
            if kubeconfig is None:
                kubeconfig = '~/.kube/config'
            client_config = yaml.load(open(os.path.expanduser(kubeconfig), 'r'))
        except IOError:
            # eat IOError, since we are only trying to read in the file if
            # it doesn't exist
            pass
        except yaml.YAMLError:
            raise WrapperException(msg="Could not parse kubeconfig: {0}".format(kubeconfig))

        config_curr_context = None
        if client_config is not None:
            config_curr_context = client_config.get('current-context')

        config_context = None
        config_cluster_name = None
        config_user_name = None
        if config_curr_context is not None:
            for entry in client_config.get('contexts'):
                if entry.get('name') == config_curr_context:
                    config_context = entry.get('context')
                    config_cluster_name = config_context.get('cluster')
                    config_user_name = config_context.get('user')

                    if namespace is None:
                        namespace = config_context.get('namespace')

        config_cluster = None
        if config_cluster_name is not None:
            for entry in client_config.get('clusters'):
                if entry.get('name') == config_cluster_name:
                    config_cluster = entry.get('cluster')
                    if api_endpoint is None:
                        api_endpoint = config_cluster.get('server')
                        if 'certificate-authority' in config_cluster:
                            certificate_authority = config_cluster.get('certificate-authority')
                        if 'certificate-authority-data' in config_cluster:
                            certificate_authority_data = config_cluster.get('certificate-authority-data')
                        if 'insecure-skip-tls-verify' in config_cluster:
                            insecure_skip_tls_verify = config_cluster.get('insecure-skip-tls-verify')

        config_user = None
        if config_user_name is not None:
            for entry in client_config.get('users'):
                if entry.get('name') == config_user_name:
                    config_user = entry.get('user')

        if username is not None and password is None:
            raise WrapperException(msg="username requires password")

        if password is not None and username is None:
            raise WrapperException(msg="password requires username")

        if username is not None and token is not None:
            raise WrapperException(msg="username and token are mutally exclusive")

        if password is not None and token is not None:
            raise WrapperException(msg="password and token are mutally exclusive")

        if username is not None and (client_cert is not None or client_key is not None):
            raise WrapperException(msg="username and client_cert/client_key are mutally exclusive")

        if password is not None and (client_cert is not None or client_key is not None):
            raise WrapperException(msg="password and client_cert/client_key are mutally exclusive")

        if token is not None and (client_cert is not None or client_key is not None):
            raise WrapperException(msg="token and client_cert/client_key are mutally exclusive")

        if client_cert is not None and client_key is None:
            raise WrapperException(msg="client_cert requires client_key")

        if client_key is not None and client_cert is None:
            raise WrapperException(msg="client_key requires client_cert")

        if config_user is not None and username is None and token is None and client_cert is None:
            username = config_user.get('username')
            password = config_user.get('password')
            token = config_user.get('token')
            client_cert = config_user.get('client-certificate')
            client_key = config_user.get('client-key')

        if api_endpoint is None:
            raise WrapperException(msg="api_endpoint is required when a kubeconfig is not provided")

        self._cluster = {'server': api_endpoint,
                         'certificate_authority': certificate_authority,
                         'certificate_authority_data': certificate_authority_data,
                         'insecure_skip_tls_verify': insecure_skip_tls_verify}
        self._user = {'username': username, 'password': password, 'token':
                      token, 'client_cert': client_cert, 'client_key': client_key}
        self._namespace = namespace
