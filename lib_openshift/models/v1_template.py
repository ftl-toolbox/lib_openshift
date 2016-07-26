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


class V1Template(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_namespaced_template',
            'namespaced': True
        },
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_template',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'update',
            'method': 'replace_namespaced_template',
            'namespaced': True
        },
        {
            'class': 'OapiV1',
            'type': 'delete',
            'method': 'delete_namespaced_template',
            'namespaced': True
        },
        {
            'class': 'OapiV1',
            'type': 'read',
            'method': 'get_namespaced_template',
            'namespaced': True
        },
    ]


    def __init__(self, kind=None, api_version=None, metadata=None, objects=None, parameters=None, labels=None):
        """
        V1Template - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'objects': 'list[RuntimeRawExtension]',
            'parameters': 'list[V1Parameter]',
            'labels': 'object'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'objects': 'objects',
            'parameters': 'parameters',
            'labels': 'labels'
        }

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._objects = objects
        self._parameters = parameters
        self._labels = labels

    @property
    def kind(self):
        """
        Gets the kind of this V1Template.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1Template.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1Template.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1Template.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1Template.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1Template.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1Template.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1Template.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1Template.
        Standard object's metadata.

        :return: The metadata of this V1Template.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1Template.
        Standard object's metadata.

        :param metadata: The metadata of this V1Template.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def objects(self):
        """
        Gets the objects of this V1Template.
        Objects is an array of objects to include in this template. Required.

        :return: The objects of this V1Template.
        :rtype: list[RuntimeRawExtension]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this V1Template.
        Objects is an array of objects to include in this template. Required.

        :param objects: The objects of this V1Template.
        :type: list[RuntimeRawExtension]
        """

        self._objects = objects

    @property
    def parameters(self):
        """
        Gets the parameters of this V1Template.
        Optional: Parameters is an array of Parameters used during the Template to Config transformation.

        :return: The parameters of this V1Template.
        :rtype: list[V1Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this V1Template.
        Optional: Parameters is an array of Parameters used during the Template to Config transformation.

        :param parameters: The parameters of this V1Template.
        :type: list[V1Parameter]
        """

        self._parameters = parameters

    @property
    def labels(self):
        """
        Gets the labels of this V1Template.
        Labels is a set of labels that are applied to every object during the Template to Config transformation. Optional

        :return: The labels of this V1Template.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this V1Template.
        Labels is a set of labels that are applied to every object during the Template to Config transformation. Optional

        :param labels: The labels of this V1Template.
        :type: object
        """

        self._labels = labels

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
