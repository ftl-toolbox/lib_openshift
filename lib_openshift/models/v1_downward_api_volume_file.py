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


class V1DownwardAPIVolumeFile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'path': 'str',
        'field_ref': 'V1ObjectFieldSelector'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'path': 'path',
        'field_ref': 'fieldRef'
    }

    def __init__(self, path=None, field_ref=None):
        """
        V1DownwardAPIVolumeFile - a model defined in Swagger

        """

        self._path = path
        self._field_ref = field_ref

    @property
    def path(self):
        """
        Gets the path of this V1DownwardAPIVolumeFile.
        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'

        :return: The path of this V1DownwardAPIVolumeFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1DownwardAPIVolumeFile.
        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'

        :param path: The path of this V1DownwardAPIVolumeFile.
        :type: str
        """

        self._path = path

    @property
    def field_ref(self):
        """
        Gets the field_ref of this V1DownwardAPIVolumeFile.
        Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.

        :return: The field_ref of this V1DownwardAPIVolumeFile.
        :rtype: V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """
        Sets the field_ref of this V1DownwardAPIVolumeFile.
        Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.

        :param field_ref: The field_ref of this V1DownwardAPIVolumeFile.
        :type: V1ObjectFieldSelector
        """

        self._field_ref = field_ref

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1DownwardAPIVolumeFile.swagger_types):
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
