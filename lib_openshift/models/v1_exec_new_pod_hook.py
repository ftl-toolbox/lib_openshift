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


class V1ExecNewPodHook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, command=None, env=None, container_name=None, volumes=None):
        """
        V1ExecNewPodHook - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'command': 'list[str]',
            'env': 'list[V1EnvVar]',
            'container_name': 'str',
            'volumes': 'list[str]'
        }

        self.attribute_map = {
            'command': 'command',
            'env': 'env',
            'container_name': 'containerName',
            'volumes': 'volumes'
        }

        self.operations = [
        ]

        self._command = command
        self._env = env
        self._container_name = container_name
        self._volumes = volumes

    @property
    def command(self):
        """
        Gets the command of this V1ExecNewPodHook.
        Command is the action command and its arguments.

        :return: The command of this V1ExecNewPodHook.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this V1ExecNewPodHook.
        Command is the action command and its arguments.

        :param command: The command of this V1ExecNewPodHook.
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """
        Gets the env of this V1ExecNewPodHook.
        Env is a set of environment variables to supply to the hook pod's container.

        :return: The env of this V1ExecNewPodHook.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1ExecNewPodHook.
        Env is a set of environment variables to supply to the hook pod's container.

        :param env: The env of this V1ExecNewPodHook.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def container_name(self):
        """
        Gets the container_name of this V1ExecNewPodHook.
        ContainerName is the name of a container in the deployment pod template whose Docker image will be used for the hook pod's container.

        :return: The container_name of this V1ExecNewPodHook.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """
        Sets the container_name of this V1ExecNewPodHook.
        ContainerName is the name of a container in the deployment pod template whose Docker image will be used for the hook pod's container.

        :param container_name: The container_name of this V1ExecNewPodHook.
        :type: str
        """

        self._container_name = container_name

    @property
    def volumes(self):
        """
        Gets the volumes of this V1ExecNewPodHook.
        Volumes is a list of named volumes from the pod template which should be copied to the hook pod. Volumes names not found in pod spec are ignored. An empty list means no volumes will be copied.

        :return: The volumes of this V1ExecNewPodHook.
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1ExecNewPodHook.
        Volumes is a list of named volumes from the pod template which should be copied to the hook pod. Volumes names not found in pod spec are ignored. An empty list means no volumes will be copied.

        :param volumes: The volumes of this V1ExecNewPodHook.
        :type: list[str]
        """

        self._volumes = volumes

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
