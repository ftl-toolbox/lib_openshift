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


class V1SecretBuildSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, secret=None, destination_dir=None):
        """
        V1SecretBuildSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'secret': 'V1LocalObjectReference',
            'destination_dir': 'str'
        }

        self.attribute_map = {
            'secret': 'secret',
            'destination_dir': 'destinationDir'
        }

        self.operations = [
        ]

        self._secret = secret
        self._destination_dir = destination_dir

    @property
    def secret(self):
        """
        Gets the secret of this V1SecretBuildSource.
        Secret is a reference to an existing secret that you want to use in your build.

        :return: The secret of this V1SecretBuildSource.
        :rtype: V1LocalObjectReference
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1SecretBuildSource.
        Secret is a reference to an existing secret that you want to use in your build.

        :param secret: The secret of this V1SecretBuildSource.
        :type: V1LocalObjectReference
        """

        self._secret = secret

    @property
    def destination_dir(self):
        """
        Gets the destination_dir of this V1SecretBuildSource.
        DestinationDir is the directory where the files from the secret should be available for the build time. For the Source build strategy, these will be injected into a container where the assemble script runs. Later, when the script finishes, all files injected will be truncated to zero length. For the Docker build strategy, these will be copied into the build directory, where the Dockerfile is located, so users can ADD or COPY them during docker build.

        :return: The destination_dir of this V1SecretBuildSource.
        :rtype: str
        """
        return self._destination_dir

    @destination_dir.setter
    def destination_dir(self, destination_dir):
        """
        Sets the destination_dir of this V1SecretBuildSource.
        DestinationDir is the directory where the files from the secret should be available for the build time. For the Source build strategy, these will be injected into a container where the assemble script runs. Later, when the script finishes, all files injected will be truncated to zero length. For the Docker build strategy, these will be copied into the build directory, where the Dockerfile is located, so users can ADD or COPY them during docker build.

        :param destination_dir: The destination_dir of this V1SecretBuildSource.
        :type: str
        """

        self._destination_dir = destination_dir

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
