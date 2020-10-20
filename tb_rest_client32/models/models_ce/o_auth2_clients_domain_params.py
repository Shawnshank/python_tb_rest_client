# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import pprint
import re  # noqa: F401

import six


class OAuth2ClientsDomainParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_registrations': 'list[ClientRegistrationDto]',
        'domain_infos': 'list[DomainInfo]'
    }

    attribute_map = {
        'client_registrations': 'clientRegistrations',
        'domain_infos': 'domainInfos'
    }

    def __init__(self, client_registrations=None, domain_infos=None):  # noqa: E501
        """OAuth2ClientsDomainParams - a model defined in Swagger"""  # noqa: E501

        self._client_registrations = None
        self._domain_infos = None
        self.discriminator = None

        if client_registrations is not None:
            self.client_registrations = client_registrations
        if domain_infos is not None:
            self.domain_infos = domain_infos

    @property
    def client_registrations(self):
        """Gets the client_registrations of this OAuth2ClientsDomainParams.  # noqa: E501


        :return: The client_registrations of this OAuth2ClientsDomainParams.  # noqa: E501
        :rtype: list[ClientRegistrationDto]
        """
        return self._client_registrations

    @client_registrations.setter
    def client_registrations(self, client_registrations):
        """Sets the client_registrations of this OAuth2ClientsDomainParams.


        :param client_registrations: The client_registrations of this OAuth2ClientsDomainParams.  # noqa: E501
        :type: list[ClientRegistrationDto]
        """

        self._client_registrations = client_registrations

    @property
    def domain_infos(self):
        """Gets the domain_infos of this OAuth2ClientsDomainParams.  # noqa: E501


        :return: The domain_infos of this OAuth2ClientsDomainParams.  # noqa: E501
        :rtype: list[DomainInfo]
        """
        return self._domain_infos

    @domain_infos.setter
    def domain_infos(self, domain_infos):
        """Sets the domain_infos of this OAuth2ClientsDomainParams.


        :param domain_infos: The domain_infos of this OAuth2ClientsDomainParams.  # noqa: E501
        :type: list[DomainInfo]
        """

        self._domain_infos = domain_infos

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(OAuth2ClientsDomainParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OAuth2ClientsDomainParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other