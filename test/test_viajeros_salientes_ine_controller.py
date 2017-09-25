# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestViajerosSalientesINEController(BaseTestCase):
    """ ViajerosSalientesINEController integration test stubs """

    def test_obtener_cantidad_total_viajeros_salientes_de_ciudad_anio(self):
        """
        Test case for obtener_cantidad_total_viajeros_salientes_de_ciudad_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad de forma total durante ese año
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/ViajerosSalientes/ObtenerCantidadTotalTuristasDeCiudadAnio/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_viajeros_salientes_de_ciudad_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_viajeros_salientes_de_ciudad_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad de forma total durante ese año de forma mensual
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/ViajerosSalientes/ObtenerCantidadTuristasDeCiudadAnioMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_viajeros_salientes_de_ciudad_rango_anios(self):
        """
        Test case for obtener_cantidad_viajeros_salientes_de_ciudad_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que salen de esa ciudad de forma total durante esos años
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2005)]
        response = self.client.open('/server/INE/ViajerosSalientes/ObtenerCantidadTuristasDeCiudadRangoAnios/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_viajeros_salientes_de_ciudad_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_viajeros_salientes_de_ciudad_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que salen de esa ciudad de forma total durante esos años 
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2005)]
        response = self.client.open('/server/INE/ViajerosSalientes/ObtenerCantidadTuristasDeCiudadRangoAniosMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_viajeros_salientes_de_ciudad_rango_anios_mes(self):
        """
        Test case for obtener_cantidad_viajeros_salientes_de_ciudad_rango_anios_mes

        Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que salen de esa ciudad de forma global durante esos años en ese mismo mes
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2005),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/ViajerosSalientes/ObtenerCantidadTuristasDeCiudadRangoAniosMes/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
