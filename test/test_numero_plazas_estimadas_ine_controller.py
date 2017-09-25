# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestNumeroPlazasEstimadasINEController(BaseTestCase):
    """ NumeroPlazasEstimadasINEController integration test stubs """

    def test_obtener_cantidad_total_plazas_estimadas_en_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_plazas_estimadas_en_ciudad_en_anio

        Dado una ciudad y un año obtiene el numero de plazas estimadas en dicha ciudad en ese año
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/NumeroPlazasEstimadas/ObtenerCantidadTotalPlazasEstimadasEnCiudadEnAnio/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_plazas_estimadas_en_ciudad_en_anio_mensualmente_dividido_por_meses(self):
        """
        Test case for obtener_cantidad_total_plazas_estimadas_en_ciudad_en_anio_mensualmente_dividido_por_meses

        Dado una ciudad y un año obtiene el numero de plazas estimadas en dicha ciudad en ese año dividido por meses
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/NumeroPlazasEstimadas/ObtenerCantidadTotalNumeroPlazasEstimadasEnCiudadEnAnioMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_plazas_estimadas_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_total_plazas_estimadas_en_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene el numero de plazas estimadas en dicha ciudad en esos años
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/NumeroPlazasEstimadas/ObtenerCantidadTotalNumeroPlazasEstimadasEnCiudadEnRangoAnios/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_plazas_estimadas_en_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_total_plazas_estimadas_en_ciudad_en_rango_anios_en_mes

        Dado una ciudad, un mes y un rango de años obtiene el numero de plazas estimadas en dicha ciudad en esos años en ese mes
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/NumeroPlazasEstimadas/ObtenerCantidadTotalNumeroPlazasEstimadasEnCiudadEnRangoAniosEnMes/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
