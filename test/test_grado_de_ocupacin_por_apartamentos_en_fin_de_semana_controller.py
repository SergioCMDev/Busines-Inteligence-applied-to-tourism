# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGradoDeOcupacinPorApartamentosEnFinDeSemanaController(BaseTestCase):
    """ GradoDeOcupacinPorApartamentosEnFinDeSemanaController integration test stubs """

    def test_obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_anio(self):
        """
        Test case for obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_anio

        Dado una ciudad y un año obtiene el porcentaje del grado de ocupación por apartamentos en fin de semana  en dicha ciudad en ese año
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/PorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemana/ObtenerPorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemanaEnCiudadEnAnio/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_anio_mensualmente dividido por meses(self):
        """
        Test case for obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_anio_mensualmente dividido por meses

        Dado una ciudad y un año obtiene el porcentaje del grado de ocupación por apartamentos en fin de semana en dicha ciudad en ese año dividido por meses
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/PorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemana/ObtenerCantidadTotalPorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en fin de semana en dicha ciudad en esos años
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/PorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemana/ObtenerCantidadTotalPorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemanaEnCiudadEnRangoAnios/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_porcentaje_del_grado_de_ocupación_por_apartamentos_en_fin_de_semana_en_ciudad_en_rango_anios_en_mes

        Dado una ciudad, un mes y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en fin de semana en fin de semana en dicha ciudad en esos años en ese mes
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/PorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemana/ObtenerCantidadTotalPorcentajeDeGradoDeOcupaciónPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosEnMes/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
