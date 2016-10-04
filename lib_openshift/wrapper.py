from __future__ import absolute_import
import os
import yaml
import json
import importlib
import string
import time
from .api_client import ApiClient
from .rest import ApiException
from .models import V1ObjectMeta,V1DeleteOptions
from .apis import ApiV1,OapiV1
from lib_openshift import models
from lib_openshift import apis

class WrapperException(Exception):

    def __init__(self, msg, **kwargs):
        self.msg = msg
        self.value = kwargs
        self.value['msg'] = msg

    def __str__(self):
        return json.dumps(self.value)


class Wrapper(object):

    def _validate_common_args(self, model, namespace=None,
                              name=None, labels=None,
                              annotations=None, state='present'):
        # TODO: validate name against k8s limitations
        if name is None:
            raise WrapperException(msg="name is required")

        if state not in ('present', 'absent'):
            raise WrapperException(msg="Unknown state: {0}".format(state))

        if labels is not None and not isinstance(labels, dict):
            raise WrapperException(msg="labels must be a dict")

        if annotations is not None and not isinstance(annotations, dict):
            raise WrapperException(msg="annotations must be a dict")

        crud_ops = self._get_crud_ops(model)
        namespaced = crud_ops['read']['namespaced']
        if namespaced and namespace is None:
            raise WrapperException(msg="namespace is required")


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


    def _get_api_client(self):
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
        return api_client


    def _get_api(self, api_class, api_client=None):
        if api_client is None:
            api_client = self._get_api_client()

        api_class_obj = getattr(apis, api_class)
        api = api_class_obj(api_client=api_client)
        return api

    def _get_k8s_object(self, model, name, namespace):
        crud_ops = self._get_crud_ops(model)
        api = self._get_api(crud_ops['read']['class'])
        method = crud_ops['read']['method']

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

    def _metadata_equals(self, existing, desired):
        attrs_to_ignore = ('creation_timestamp', 'resource_version',
                           'self_link', 'uid')
        for attribute in existing.attribute_map.keys():
            if attribute in attrs_to_ignore:
                next
            elif attribute == 'annotations':
                existing_annotations = existing.annotations
                desired_annotations = desired.annotations
                if existing_annotations is None:
                    existing_annotations = {}
                if desired_annotations is None:
                    desired_annotations = {}
                if existing_annotations == desired_annotations:
                    next
                for scc_attr in ('mcs', 'supplemental-groups', 'uid-range'):
                    scc_key = "openshift.io/sa.scc.{0}".format(scc_attr)
                    if scc_key in existing_annotations:
                        if scc_key in desired_annotations:
                            if existing_annotations[scc_key] != desired_annotations[scc_key]:
                                return False
            elif getattr(existing, attribute) is None and getattr(desired, attribute) is not None:
                return False
            elif getattr(desired, attribute) is None and getattr(existing, attribute) is not None:
                return False
            elif getattr(existing, attribute) != getattr(desired, attribute):
                return False
        return True

    def _merge_metadata(self, existing, desired):
        return existing

    def _k8s_objects_equals(self, existing, desired):
        for attribute in existing.attribute_map.keys():
            if attribute == 'metadata':
                if not self._metadata_equals(existing.metadata, desired.metadata):
                    import pdb; pdb.set_trace()
                    return False
            elif attribute == 'status':
                next
            elif existing.kind == 'Namespace' and attribute == 'spec':
                if existing.spec.finalizers is not None and (desired.spec is None):
                    if len(existing.spec.finalizers) == 1 and len(existing.spec.finalizers[0].to_dict()) != 0:
                        import pdb; pdb.set_trace()
                        return False
                elif existing.spec != desired.spec:
                    import pdb; pdb.set_trace()
                    return False
            elif getattr(existing, attribute) is None and getattr(desired, attribute) is not None:
                import pdb; pdb.set_trace()
                return False
            elif getattr(desired, attribute) is None and getattr(existing, attribute) is not None:
                import pdb; pdb.set_trace()
                return False
            elif getattr(existing, attribute) != getattr(desired, attribute):
                import pdb; pdb.set_trace()
                return False

        return True

    def _merge_k8s_object_for_update(self, existing, desired):
        return existing

    def _create_or_update_k8s_object(self, model, k8s_object,
                                     body, namespace):
        changed = False
        result = {}
        crud_ops = self._get_crud_ops(model)
        api = self._get_api(crud_ops['create']['class'])
        create_method = crud_ops['create']['method']
        update_method = crud_ops['update']['method']

        if k8s_object is not None:
#            if self._k8s_objects_equals(k8s_object, body):
#                changed = False
#                result = k8s_object
#            else:
#                merged = _merge_k8s_object_for_update(k8s_object, body)
#                try:
#                    if namespace is None:
#                        k8s_object = getattr(api, update_method)(merged)
#                    else:
#                        k8s_object = getattr(api, update_method)(merged, namespace)
#                    changed = True
#                    result = k8s_object.to_dict()
#                except ApiException as e:
#                    raise WrapperException(msg="api request failed code: {0}, {1}".format(e.status, e))
#
            changed = False
            result = k8s_object.to_dict()
        else:
            try:
                if namespace is None:
                    k8s_object = getattr(api, create_method)(body)
                else:
                    k8s_object = getattr(api, create_method)(body, namespace)
                changed = True
                result = k8s_object.to_dict()
            except ApiException as e:
                raise WrapperException(msg="api request failed code: {0}, {1}".format(e.status, e))
        return (changed, result)

    def _delete_k8s_object(self, model, k8s_object,
                           delete_options, name, namespace):
        crud_ops = self._get_crud_ops(model)
        api = self._get_api(crud_ops['delete']['class'])
        delete_method = crud_ops['delete']['method']
        changed = False
        status = {}
        if k8s_object is not None:
            try:
                if k8s_object.kind in ('Service'):
                    status = getattr(api, delete_method)(namespace, name).to_dict()
                else:
                    if namespace is None:
                        status = getattr(api, delete_method)(delete_options,
                                                             name).to_dict()
                    else:
                        status = getattr(api, delete_method)(delete_options,
                                                             namespace, name).to_dict()
                changed = True
            except ApiException as e:
                raise WrapperException(msg="api request failed code: {0}, reason: {1}".format(e.status, e.reason))
        return (changed, status)


    def _k8s_object(self, model, namespace, name, api_version,
                    labels, annotations, state, **model_kwargs):

        friendly_name = model.__name__.replace(api_version.capitalize(), '')

        k8s_object = self._get_k8s_object(model, name, namespace)

        # TODO: add check mode
        if state == 'present':
            if namespace is not None:
                self.namespace(name=namespace, api_version=api_version, state='present')
            metadata = Wrapper.metadata_from_datastructure(api_version, name=name,
                                                           labels=labels, annotations=annotations)
            body = model(kind=friendly_name, api_version=api_version,
                         metadata=metadata, **model_kwargs)
            (changed, result) = self._create_or_update_k8s_object(model,
                                                                  k8s_object,
                                                                  body, namespace)

        elif state == 'absent':
            delete_options = V1DeleteOptions()
            (changed, result) = self._delete_k8s_object(model,
                                                        k8s_object, delete_options,
                                                        name, namespace)

        # TODO: implement proper wait on object creation
        time.sleep(.1)
        return {'changed': changed, friendly_name.lower(): result}

#    def namespace(self, name=None, api_version='v1', labels=None,
#                  annotations=None, state='present'):
#        self._validate_common_args(False, None, name, labels, annotations, state)

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
    def translate_params(model, **kwargs):
        '''Translate kwargs to parameters of the model's constructor
        Args:
            model(class): class which constructor needs to be translated to
        Returns:
            dict of parameters ready to use in the constructor.
        '''
        res = {}
        for i,param in enumerate(model.__init__.__code__.co_varnames):
            if param in kwargs:
                res[param] = kwargs[param]
        return res

    @staticmethod
    def get_child_models(model):
        '''Get the list of child models for the current model
        Args:
            model: model class
        Returns:
            a list of tuples (attribute, class, child_type), where
        attribute is the name of the child attribute, class - the class
        name of the child model, child_type - list if the child is a list
        '''
        res = []
        for attr, swagger_t in model.swagger_types.iteritems():
            if swagger_t in ['str', 'int', 'object', 'bool', 'list[str]']:
                continue
            if swagger_t.startswith('list['):
                child_type = 'list'
                child_model = swagger_t[5:-1]
            else:
                child_type = None
                child_model = swagger_t
            res.append((attr, child_model, child_type))
        return res

    @staticmethod
    def k8s_obj_spec_from_datastructure(object_name, **kwargs):
        '''Create spec ready to be used in the object.
        Args:
            api_version(str): version of the api
            kwargs: object description
        '''
        if kwargs['api_version'] == 'v1':
            spec_model_name = kwargs['api_version'].capitalize() + string.capwords(object_name, '_').replace('_', '') + 'Spec'
            spec_model = getattr(models, spec_model_name)
        else:
            raise WrapperException(msg="unsupported api version: {0}".format(api_version))

        params = Wrapper.translate_params(spec_model, **kwargs)
        child_models_list = Wrapper.get_child_models(spec_model)
        for ch_model in child_models_list:
            if ch_model[1] in kwargs.copy():
                if isinstance(kwargs[ch_model[1]], list):
                    cur_spec = []
                    for child in kwargs[ch_model[1]]:
                        cur_spec.append(k8s_obj_spec_from_datastructure(ch_model[2], child))
                else:
                    cur_spec = k8s_obj_spec_from_datastructure(ch_model[2], kwargs[ch_model[1]])
                kwargs[ch_model[1]] = cur_spec

        spec = spec_model(**params)
        return spec

    def __getattr__(self, name):
        def obj_mapper(**kwargs):
            if 'kind' in kwargs:
                del kwargs['kind']
            return self.k8s_object(kind=name, **kwargs)

        return obj_mapper


    def k8s_object(self, **kwargs):
        # TODO: Distinguish the object topology and import nested objects as needed!
        kind = kwargs['kind']
        api_version = kwargs.setdefault('api_version', 'v1')

        camelName = string.capwords(kind, '_').replace('_', '')
        model_name = api_version.capitalize() + camelName
        if model_name not in dir(models):
            raise WrapperException(msg="unsupported k8s object: {0}".format(name))

        model = getattr(models, model_name)
        obj_spec = Wrapper.k8s_obj_spec_from_datastructure(kind, **kwargs)

        namespace = kwargs.get('namespace', None)
        name = kwargs.get('name', None)
        labels = kwargs.get('labels',{})
        annotations = kwargs.get('annotations', {})
        state = kwargs.get('state', 'present')

        self._validate_common_args(model, namespace, name, labels, annotations, state)

        return self._k8s_object(model, namespace, name, api_version,
                                labels, annotations, state, spec=obj_spec)


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
