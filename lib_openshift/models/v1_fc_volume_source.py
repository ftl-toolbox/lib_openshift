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


class V1FCVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, target_ww_ns=None, lun=None, fs_type=None, read_only=None):
        """
        V1FCVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'target_ww_ns': 'list[str]',
            'lun': 'int',
            'fs_type': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'target_ww_ns': 'targetWWNs',
            'lun': 'lun',
            'fs_type': 'fsType',
            'read_only': 'readOnly'
        }

        self.operations = [
        ]

        self._target_ww_ns = target_ww_ns
        self._lun = lun
        self._fs_type = fs_type
        self._read_only = read_only

    @property
    def target_ww_ns(self):
        """
        Gets the target_ww_ns of this V1FCVolumeSource.
        Required: FC target world wide names (WWNs)

        :return: The target_ww_ns of this V1FCVolumeSource.
        :rtype: list[str]
        """
        return self._target_ww_ns

    @target_ww_ns.setter
    def target_ww_ns(self, target_ww_ns):
        """
        Sets the target_ww_ns of this V1FCVolumeSource.
        Required: FC target world wide names (WWNs)

        :param target_ww_ns: The target_ww_ns of this V1FCVolumeSource.
        :type: list[str]
        """

        self._target_ww_ns = target_ww_ns

    @property
    def lun(self):
        """
        Gets the lun of this V1FCVolumeSource.
        Required: FC target lun number

        :return: The lun of this V1FCVolumeSource.
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """
        Sets the lun of this V1FCVolumeSource.
        Required: FC target lun number

        :param lun: The lun of this V1FCVolumeSource.
        :type: int
        """

        self._lun = lun

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1FCVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.

        :return: The fs_type of this V1FCVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1FCVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.

        :param fs_type: The fs_type of this V1FCVolumeSource.
        :type: str
        """

        self._fs_type = fs_type

    @property
    def read_only(self):
        """
        Gets the read_only of this V1FCVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :return: The read_only of this V1FCVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1FCVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :param read_only: The read_only of this V1FCVolumeSource.
        :type: bool
        """

        self._read_only = read_only

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
