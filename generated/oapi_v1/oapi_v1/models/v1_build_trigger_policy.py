# coding: utf-8

"""
    OpenShift v1 REST API

    The OpenShift API exposes operations for managing an enterprise Kubernetes cluster, including security and user management, application deployments, image and source builds, HTTP(s) routing, and project management.

    OpenAPI spec version: v1
    
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


class V1BuildTriggerPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, github=None, generic=None, image_change=None):
        """
        V1BuildTriggerPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'github': 'V1WebHookTrigger',
            'generic': 'V1WebHookTrigger',
            'image_change': 'V1ImageChangeTrigger'
        }

        self.attribute_map = {
            'type': 'type',
            'github': 'github',
            'generic': 'generic',
            'image_change': 'imageChange'
        }

        self._type = type
        self._github = github
        self._generic = generic
        self._image_change = image_change

    @property
    def type(self):
        """
        Gets the type of this V1BuildTriggerPolicy.
        Type is the type of build trigger

        :return: The type of this V1BuildTriggerPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1BuildTriggerPolicy.
        Type is the type of build trigger

        :param type: The type of this V1BuildTriggerPolicy.
        :type: str
        """

        self._type = type

    @property
    def github(self):
        """
        Gets the github of this V1BuildTriggerPolicy.
        GitHubWebHook contains the parameters for a GitHub webhook type of trigger

        :return: The github of this V1BuildTriggerPolicy.
        :rtype: V1WebHookTrigger
        """
        return self._github

    @github.setter
    def github(self, github):
        """
        Sets the github of this V1BuildTriggerPolicy.
        GitHubWebHook contains the parameters for a GitHub webhook type of trigger

        :param github: The github of this V1BuildTriggerPolicy.
        :type: V1WebHookTrigger
        """

        self._github = github

    @property
    def generic(self):
        """
        Gets the generic of this V1BuildTriggerPolicy.
        GenericWebHook contains the parameters for a Generic webhook type of trigger

        :return: The generic of this V1BuildTriggerPolicy.
        :rtype: V1WebHookTrigger
        """
        return self._generic

    @generic.setter
    def generic(self, generic):
        """
        Sets the generic of this V1BuildTriggerPolicy.
        GenericWebHook contains the parameters for a Generic webhook type of trigger

        :param generic: The generic of this V1BuildTriggerPolicy.
        :type: V1WebHookTrigger
        """

        self._generic = generic

    @property
    def image_change(self):
        """
        Gets the image_change of this V1BuildTriggerPolicy.
        ImageChange contains parameters for an ImageChange type of trigger

        :return: The image_change of this V1BuildTriggerPolicy.
        :rtype: V1ImageChangeTrigger
        """
        return self._image_change

    @image_change.setter
    def image_change(self, image_change):
        """
        Sets the image_change of this V1BuildTriggerPolicy.
        ImageChange contains parameters for an ImageChange type of trigger

        :param image_change: The image_change of this V1BuildTriggerPolicy.
        :type: V1ImageChangeTrigger
        """

        self._image_change = image_change

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