# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Body6(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anio: int=None, ciudad: str=None, cantidad: int=None):
        """
        Body6 - a model defined in Swagger

        :param anio: The anio of this Body6.
        :type anio: int
        :param ciudad: The ciudad of this Body6.
        :type ciudad: str
        :param cantidad: The cantidad of this Body6.
        :type cantidad: int
        """
        self.swagger_types = {
            'anio': int,
            'ciudad': str,
            'cantidad': int
        }

        self.attribute_map = {
            'anio': 'Anio',
            'ciudad': 'Ciudad',
            'cantidad': 'Cantidad'
        }

        self._anio = anio
        self._ciudad = ciudad
        self._cantidad = cantidad

    @classmethod
    def from_dict(cls, dikt) -> 'Body6':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body6 of this Body6.
        :rtype: Body6
        """
        return deserialize_model(dikt, cls)

    @property
    def anio(self) -> int:
        """
        Gets the anio of this Body6.

        :return: The anio of this Body6.
        :rtype: int
        """
        return self._anio

    @anio.setter
    def anio(self, anio: int):
        """
        Sets the anio of this Body6.

        :param anio: The anio of this Body6.
        :type anio: int
        """

        self._anio = anio

    @property
    def ciudad(self) -> str:
        """
        Gets the ciudad of this Body6.

        :return: The ciudad of this Body6.
        :rtype: str
        """
        return self._ciudad

    @ciudad.setter
    def ciudad(self, ciudad: str):
        """
        Sets the ciudad of this Body6.

        :param ciudad: The ciudad of this Body6.
        :type ciudad: str
        """

        self._ciudad = ciudad

    @property
    def cantidad(self) -> int:
        """
        Gets the cantidad of this Body6.

        :return: The cantidad of this Body6.
        :rtype: int
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        """
        Sets the cantidad of this Body6.

        :param cantidad: The cantidad of this Body6.
        :type cantidad: int
        """

        self._cantidad = cantidad

