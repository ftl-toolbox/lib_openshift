# coding: utf-8

"""
    

    

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1ServiceAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'ApiV1',
            'type': 'create',
            'method': 'create_namespaced_serviceaccount',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'create',
            'method': 'create_serviceaccount',
            'namespaced': False
        },
        {
            'class': 'ApiV1',
            'type': 'update',
            'method': 'replace_namespaced_serviceaccount',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'delete',
            'method': 'delete_namespaced_serviceaccount',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'read',
            'method': 'get_namespaced_serviceaccount',
            'namespaced': True
        },
    ]


    def __init__(self, kind=None, api_version=None, metadata=None, secrets=None, image_pull_secrets=None):
        """
        V1ServiceAccount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'secrets': 'list[V1ObjectReference]',
            'image_pull_secrets': 'list[V1LocalObjectReference]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'secrets': 'secrets',
            'image_pull_secrets': 'imagePullSecrets'
        }

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._secrets = secrets
        self._image_pull_secrets = image_pull_secrets

    @property
    def kind(self):
        """
        Gets the kind of this V1ServiceAccount.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ServiceAccount.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ServiceAccount.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ServiceAccount.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ServiceAccount.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ServiceAccount.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ServiceAccount.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ServiceAccount.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ServiceAccount.
        Standard object's metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1ServiceAccount.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ServiceAccount.
        Standard object's metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1ServiceAccount.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def secrets(self):
        """
        Gets the secrets of this V1ServiceAccount.
        Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: http://releases.k8s.io/release-1.2/docs/user-guide/secrets.md

        :return: The secrets of this V1ServiceAccount.
        :rtype: list[V1ObjectReference]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """
        Sets the secrets of this V1ServiceAccount.
        Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: http://releases.k8s.io/release-1.2/docs/user-guide/secrets.md

        :param secrets: The secrets of this V1ServiceAccount.
        :type: list[V1ObjectReference]
        """

        self._secrets = secrets

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this V1ServiceAccount.
        ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: http://releases.k8s.io/release-1.2/docs/user-guide/secrets.md#manually-specifying-an-imagepullsecret

        :return: The image_pull_secrets of this V1ServiceAccount.
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this V1ServiceAccount.
        ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: http://releases.k8s.io/release-1.2/docs/user-guide/secrets.md#manually-specifying-an-imagepullsecret

        :param image_pull_secrets: The image_pull_secrets of this V1ServiceAccount.
        :type: list[V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
