# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class Role(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Role - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'permission_set': 'PermissionSet',
            'model_set': 'ModelSet',
            'url': 'str',
            'users_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'permission_set': 'permission_set',
            'model_set': 'model_set',
            'url': 'url',
            'users_url': 'users_url'
        }

        self._id = None
        self._name = None
        self._permission_set = None
        self._model_set = None
        self._url = None
        self._users_url = None

    @property
    def id(self):
        """
        Gets the id of this Role.
        Unique Id

        :return: The id of this Role.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Role.
        Unique Id

        :param id: The id of this Role.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Role.
        Name of Role

        :return: The name of this Role.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Role.
        Name of Role

        :param name: The name of this Role.
        :type: str
        """
        
        self._name = name

    @property
    def permission_set(self):
        """
        Gets the permission_set of this Role.


        :return: The permission_set of this Role.
        :rtype: PermissionSet
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """
        Sets the permission_set of this Role.


        :param permission_set: The permission_set of this Role.
        :type: PermissionSet
        """
        
        self._permission_set = permission_set

    @property
    def model_set(self):
        """
        Gets the model_set of this Role.


        :return: The model_set of this Role.
        :rtype: ModelSet
        """
        return self._model_set

    @model_set.setter
    def model_set(self, model_set):
        """
        Sets the model_set of this Role.


        :param model_set: The model_set of this Role.
        :type: ModelSet
        """
        
        self._model_set = model_set

    @property
    def url(self):
        """
        Gets the url of this Role.
        Link to get this item

        :return: The url of this Role.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Role.
        Link to get this item

        :param url: The url of this Role.
        :type: str
        """
        
        self._url = url

    @property
    def users_url(self):
        """
        Gets the users_url of this Role.
        Link to get list of users with this role

        :return: The users_url of this Role.
        :rtype: str
        """
        return self._users_url

    @users_url.setter
    def users_url(self, users_url):
        """
        Sets the users_url of this Role.
        Link to get list of users with this role

        :param users_url: The users_url of this Role.
        :type: str
        """
        
        self._users_url = users_url

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

