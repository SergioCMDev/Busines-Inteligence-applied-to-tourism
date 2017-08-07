# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Body(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anio: int=None, cantidad: int=None):
        """
        Body - a model defined in Swagger

        :param anio: The anio of this Body.
        :type anio: int
        :param cantidad: The cantidad of this Body.
        :type cantidad: int
        """
        self.swagger_types = {
            'anio': int,
            'cantidad': int
        }

        self.attribute_map = {
            'anio': 'Anio',
            'cantidad': 'Cantidad'
        }

        self._anio = anio
        self._cantidad = cantidad

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.
        :rtype: Body
        """
        return deserialize_model(dikt, cls)

    @property
    def anio(self) -> int:
        """
        Gets the anio of this Body.

        :return: The anio of this Body.
        :rtype: int
        """
        return self._anio

    @anio.setter
    def anio(self, anio: int):
        """
        Sets the anio of this Body.

        :param anio: The anio of this Body.
        :type anio: int
        """

        self._anio = anio

    @property
    def cantidad(self) -> int:
        """
        Gets the cantidad of this Body.

        :return: The cantidad of this Body.
        :rtype: int
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        """
        Sets the cantidad of this Body.

        :param cantidad: The cantidad of this Body.
        :type cantidad: int
        """

        self._cantidad = cantidad
