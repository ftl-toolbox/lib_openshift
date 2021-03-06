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


class V1OAuthClient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_oauthclient',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'update',
            'method': 'replace_oauthclient',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'delete',
            'method': 'delete_oauthclient',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'read',
            'method': 'get_oauthclient',
            'namespaced': False
        },
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'V1ObjectMeta',
        'secret': 'str',
        'respond_with_challenges': 'bool',
        'redirect_ur_is': 'list[str]'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'secret': 'secret',
        'respond_with_challenges': 'respondWithChallenges',
        'redirect_ur_is': 'redirectURIs'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, secret=None, respond_with_challenges=None, redirect_ur_is=None):
        """
        V1OAuthClient - a model defined in Swagger

        """

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._secret = secret
        self._respond_with_challenges = respond_with_challenges
        self._redirect_ur_is = redirect_ur_is

    @property
    def kind(self):
        """
        Gets the kind of this V1OAuthClient.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1OAuthClient.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1OAuthClient.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1OAuthClient.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1OAuthClient.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1OAuthClient.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1OAuthClient.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1OAuthClient.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1OAuthClient.
        Standard object's metadata.

        :return: The metadata of this V1OAuthClient.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1OAuthClient.
        Standard object's metadata.

        :param metadata: The metadata of this V1OAuthClient.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def secret(self):
        """
        Gets the secret of this V1OAuthClient.
        Secret is the unique secret associated with a client

        :return: The secret of this V1OAuthClient.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this V1OAuthClient.
        Secret is the unique secret associated with a client

        :param secret: The secret of this V1OAuthClient.
        :type: str
        """

        self._secret = secret

    @property
    def respond_with_challenges(self):
        """
        Gets the respond_with_challenges of this V1OAuthClient.
        RespondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects

        :return: The respond_with_challenges of this V1OAuthClient.
        :rtype: bool
        """
        return self._respond_with_challenges

    @respond_with_challenges.setter
    def respond_with_challenges(self, respond_with_challenges):
        """
        Sets the respond_with_challenges of this V1OAuthClient.
        RespondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects

        :param respond_with_challenges: The respond_with_challenges of this V1OAuthClient.
        :type: bool
        """

        self._respond_with_challenges = respond_with_challenges

    @property
    def redirect_ur_is(self):
        """
        Gets the redirect_ur_is of this V1OAuthClient.
        RedirectURIs is the valid redirection URIs associated with a client

        :return: The redirect_ur_is of this V1OAuthClient.
        :rtype: list[str]
        """
        return self._redirect_ur_is

    @redirect_ur_is.setter
    def redirect_ur_is(self, redirect_ur_is):
        """
        Sets the redirect_ur_is of this V1OAuthClient.
        RedirectURIs is the valid redirection URIs associated with a client

        :param redirect_ur_is: The redirect_ur_is of this V1OAuthClient.
        :type: list[str]
        """

        self._redirect_ur_is = redirect_ur_is

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1OAuthClient.swagger_types):
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
