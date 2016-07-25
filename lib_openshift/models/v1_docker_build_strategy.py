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


class V1DockerBuildStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, pull_secret=None, no_cache=None, env=None, force_pull=None, dockerfile_path=None):
        """
        V1DockerBuildStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'V1ObjectReference',
            'pull_secret': 'V1LocalObjectReference',
            'no_cache': 'bool',
            'env': 'list[V1EnvVar]',
            'force_pull': 'bool',
            'dockerfile_path': 'str'
        }

        self.attribute_map = {
            '_from': 'from',
            'pull_secret': 'pullSecret',
            'no_cache': 'noCache',
            'env': 'env',
            'force_pull': 'forcePull',
            'dockerfile_path': 'dockerfilePath'
        }

        self.operations = [
        ]

        self.__from = _from
        self._pull_secret = pull_secret
        self._no_cache = no_cache
        self._env = env
        self._force_pull = force_pull
        self._dockerfile_path = dockerfile_path

    @property
    def _from(self):
        """
        Gets the _from of this V1DockerBuildStrategy.
        From is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled the resulting image will be used in the FROM line of the Dockerfile for this build.

        :return: The _from of this V1DockerBuildStrategy.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1DockerBuildStrategy.
        From is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled the resulting image will be used in the FROM line of the Dockerfile for this build.

        :param _from: The _from of this V1DockerBuildStrategy.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def pull_secret(self):
        """
        Gets the pull_secret of this V1DockerBuildStrategy.
        PullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :return: The pull_secret of this V1DockerBuildStrategy.
        :rtype: V1LocalObjectReference
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """
        Sets the pull_secret of this V1DockerBuildStrategy.
        PullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :param pull_secret: The pull_secret of this V1DockerBuildStrategy.
        :type: V1LocalObjectReference
        """

        self._pull_secret = pull_secret

    @property
    def no_cache(self):
        """
        Gets the no_cache of this V1DockerBuildStrategy.
        NoCache if set to true indicates that the docker build must be executed with the --no-cache=true flag

        :return: The no_cache of this V1DockerBuildStrategy.
        :rtype: bool
        """
        return self._no_cache

    @no_cache.setter
    def no_cache(self, no_cache):
        """
        Sets the no_cache of this V1DockerBuildStrategy.
        NoCache if set to true indicates that the docker build must be executed with the --no-cache=true flag

        :param no_cache: The no_cache of this V1DockerBuildStrategy.
        :type: bool
        """

        self._no_cache = no_cache

    @property
    def env(self):
        """
        Gets the env of this V1DockerBuildStrategy.
        Env contains additional environment variables you want to pass into a builder container

        :return: The env of this V1DockerBuildStrategy.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1DockerBuildStrategy.
        Env contains additional environment variables you want to pass into a builder container

        :param env: The env of this V1DockerBuildStrategy.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def force_pull(self):
        """
        Gets the force_pull of this V1DockerBuildStrategy.
        ForcePull describes if the builder should pull the images from registry prior to building.

        :return: The force_pull of this V1DockerBuildStrategy.
        :rtype: bool
        """
        return self._force_pull

    @force_pull.setter
    def force_pull(self, force_pull):
        """
        Sets the force_pull of this V1DockerBuildStrategy.
        ForcePull describes if the builder should pull the images from registry prior to building.

        :param force_pull: The force_pull of this V1DockerBuildStrategy.
        :type: bool
        """

        self._force_pull = force_pull

    @property
    def dockerfile_path(self):
        """
        Gets the dockerfile_path of this V1DockerBuildStrategy.
        DockerfilePath is the path of the Dockerfile that will be used to build the Docker image, relative to the root of the context (contextDir).

        :return: The dockerfile_path of this V1DockerBuildStrategy.
        :rtype: str
        """
        return self._dockerfile_path

    @dockerfile_path.setter
    def dockerfile_path(self, dockerfile_path):
        """
        Sets the dockerfile_path of this V1DockerBuildStrategy.
        DockerfilePath is the path of the Dockerfile that will be used to build the Docker image, relative to the root of the context (contextDir).

        :param dockerfile_path: The dockerfile_path of this V1DockerBuildStrategy.
        :type: str
        """

        self._dockerfile_path = dockerfile_path

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
