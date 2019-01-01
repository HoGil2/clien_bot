# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from clien_bot.models.base_model_ import Model
from clien_bot import util


class Success(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, message: str='ok', code: int=None):  # noqa: E501
        """Success - a model defined in Swagger

        :param message: The message of this Success.  # noqa: E501
        :type message: str
        :param code: The code of this Success.  # noqa: E501
        :type code: int
        """
        self.swagger_types = {
            'message': str,
            'code': int
        }

        self.attribute_map = {
            'message': 'message',
            'code': 'code'
        }

        self._message = message
        self._code = code

    @classmethod
    def from_dict(cls, dikt) -> 'Success':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Success of this Success.  # noqa: E501
        :rtype: Success
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this Success.


        :return: The message of this Success.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Success.


        :param message: The message of this Success.
        :type message: str
        """

        self._message = message

    @property
    def code(self) -> int:
        """Gets the code of this Success.


        :return: The code of this Success.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this Success.


        :param code: The code of this Success.
        :type code: int
        """

        self._code = code
