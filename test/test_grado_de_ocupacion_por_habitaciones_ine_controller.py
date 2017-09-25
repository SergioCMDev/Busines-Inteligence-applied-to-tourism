# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGradoDeOcupacionPorHabitacionesINEController(BaseTestCase):
    """ GradoDeOcupacionPorHabitacionesINEController integration test stubs """

    def test_obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_anio(self):
        """
        Test case for obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_anio

        Dado una ciudad y un año obtiene el grado de ocupación por habitaciones en dicha ciudad en ese año
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/GradoDeOcupacionPorHabitaciones/ObtenerGradoDeOcupacionPorHabitacionesEnCiudadEnAnio/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_anio_mensualmente dividido por meses(self):
        """
        Test case for obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_anio_mensualmente dividido por meses

        Dado una ciudad y un año obtiene el grado de ocupación por habitaciones en dicha ciudad en ese año dividido por meses
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/GradoDeOcupacionPorHabitaciones/ObtenerCantidadTotalGradoDeOcupacionPorHabitacionesEnCiudadEnAnioMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene el grado de ocupación por habitaciones en dicha ciudad en esos años
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/GradoDeOcupacionPorHabitaciones/ObtenerCantidadTotalGradoDeOcupacionPorHabitacionesEnCiudadEnRangoAnios/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_grado_de_ocupación_por_habitaciones_en_ciudad_en_rango_anios_en_mes

        Dado una ciudad, un mes y un rango de años obtiene el grado de ocupación por habitaciones en dicha ciudad en esos años en ese mes
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/GradoDeOcupacionPorHabitaciones/ObtenerCantidadTotalGradoDeOcupacionPorHabitacionesEnCiudadEnRangoAniosEnMes/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
