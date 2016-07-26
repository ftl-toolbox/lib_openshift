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


class V1PersistentVolumeClaim(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'ApiV1',
            'type': 'create',
            'method': 'create_namespaced_persistentvolumeclaim',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'update',
            'method': 'replace_namespaced_persistentvolumeclaim',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'delete',
            'method': 'delete_namespaced_persistentvolumeclaim',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'read',
            'method': 'get_namespaced_persistentvolumeclaim',
            'namespaced': True
        },
        {
            'class': 'ApiV1',
            'type': 'create',
            'method': 'create_persistentvolumeclaim',
            'namespaced': False
        },
    ]


    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        """
        V1PersistentVolumeClaim - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'spec': 'V1PersistentVolumeClaimSpec',
            'status': 'V1PersistentVolumeClaimStatus'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'spec': 'spec',
            'status': 'status'
        }

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._spec = spec
        self._status = status

    @property
    def kind(self):
        """
        Gets the kind of this V1PersistentVolumeClaim.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1PersistentVolumeClaim.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1PersistentVolumeClaim.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1PersistentVolumeClaim.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1PersistentVolumeClaim.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1PersistentVolumeClaim.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1PersistentVolumeClaim.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1PersistentVolumeClaim.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1PersistentVolumeClaim.
        Standard object's metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1PersistentVolumeClaim.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1PersistentVolumeClaim.
        Standard object's metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1PersistentVolumeClaim.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self):
        """
        Gets the spec of this V1PersistentVolumeClaim.
        Spec defines the desired characteristics of a volume requested by a pod author. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :return: The spec of this V1PersistentVolumeClaim.
        :rtype: V1PersistentVolumeClaimSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """
        Sets the spec of this V1PersistentVolumeClaim.
        Spec defines the desired characteristics of a volume requested by a pod author. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :param spec: The spec of this V1PersistentVolumeClaim.
        :type: V1PersistentVolumeClaimSpec
        """

        self._spec = spec

    @property
    def status(self):
        """
        Gets the status of this V1PersistentVolumeClaim.
        Status represents the current information/status of a persistent volume claim. Read-only. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :return: The status of this V1PersistentVolumeClaim.
        :rtype: V1PersistentVolumeClaimStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1PersistentVolumeClaim.
        Status represents the current information/status of a persistent volume claim. Read-only. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :param status: The status of this V1PersistentVolumeClaim.
        :type: V1PersistentVolumeClaimStatus
        """

        self._status = status

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
