# coding: utf-8

"""
    Aspose.Storage for Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AsposeResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'status': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status'
    }

    discriminator_value_class_map = {
        '': 'CopyFileResponse',
        '': 'StorageExistResponse',
        '': 'FilesResponse',
        '': 'FileVersionsResponse',
        '': 'UploadResponse',
        '': 'DiscUsageResponse',
        '': 'FileExistResponse',
        '': 'RemoveFolderResponse',
        '': 'MoveFileResponse',
        '': 'MoveFolderResponse',
        '': 'RemoveFileResponse',
        '': 'CreateFolderResponse'
    }

    def __init__(self, code=None, status=None):
        """
        AsposeResponse - a model defined in Swagger
        """

        self._code = None
        self._status = None
        self.discriminator = 'Type'

        self.code = code
        if status is not None:
          self.status = status

    @property
    def code(self):
        """
        Gets the code of this AsposeResponse.

        :return: The code of this AsposeResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this AsposeResponse.

        :param code: The code of this AsposeResponse.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def status(self):
        """
        Gets the status of this AsposeResponse.

        :return: The status of this AsposeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AsposeResponse.

        :param status: The status of this AsposeResponse.
        :type: str
        """

        self._status = status

    def get_real_child_model(self, data):
        """
        Returns the real base class specified by the discriminator
        """
        discriminator_value = data[self.discriminator].lower()
        if self.discriminator_value_class_map.has_key(discriminator_value):
            return self.discriminator_value_class_map[discriminator_value]
        else:
            return None

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
        if not isinstance(other, AsposeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other