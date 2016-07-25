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


class V1ImageStreamImportStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _import=None, repository=None, images=None):
        """
        V1ImageStreamImportStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_import': 'V1ImageStream',
            'repository': 'V1RepositoryImportStatus',
            'images': 'list[V1ImageImportStatus]'
        }

        self.attribute_map = {
            '_import': 'import',
            'repository': 'repository',
            'images': 'images'
        }

        self.operations = [
        ]

        self.__import = _import
        self._repository = repository
        self._images = images

    @property
    def _import(self):
        """
        Gets the _import of this V1ImageStreamImportStatus.
        Import is the image stream that was successfully updated or created when 'to' was set.

        :return: The _import of this V1ImageStreamImportStatus.
        :rtype: V1ImageStream
        """
        return self.__import

    @_import.setter
    def _import(self, _import):
        """
        Sets the _import of this V1ImageStreamImportStatus.
        Import is the image stream that was successfully updated or created when 'to' was set.

        :param _import: The _import of this V1ImageStreamImportStatus.
        :type: V1ImageStream
        """

        self.__import = _import

    @property
    def repository(self):
        """
        Gets the repository of this V1ImageStreamImportStatus.
        Repository is set if spec.repository was set to the outcome of the import

        :return: The repository of this V1ImageStreamImportStatus.
        :rtype: V1RepositoryImportStatus
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """
        Sets the repository of this V1ImageStreamImportStatus.
        Repository is set if spec.repository was set to the outcome of the import

        :param repository: The repository of this V1ImageStreamImportStatus.
        :type: V1RepositoryImportStatus
        """

        self._repository = repository

    @property
    def images(self):
        """
        Gets the images of this V1ImageStreamImportStatus.
        Images is set with the result of importing spec.images

        :return: The images of this V1ImageStreamImportStatus.
        :rtype: list[V1ImageImportStatus]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this V1ImageStreamImportStatus.
        Images is set with the result of importing spec.images

        :param images: The images of this V1ImageStreamImportStatus.
        :type: list[V1ImageImportStatus]
        """

        self._images = images

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
