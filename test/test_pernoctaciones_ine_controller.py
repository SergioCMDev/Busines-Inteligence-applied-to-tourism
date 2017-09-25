# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPernoctacionesINEController(BaseTestCase):
    """ PernoctacionesINEController integration test stubs """

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_anio

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese año
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_anio

        Dado una ciudad y un año obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en ese año
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadPorcentajePernoctacionesEnCiudadEnAnio/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_anio_mensualmente dividido por meses(self):
        """
        Test case for obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_anio_mensualmente dividido por meses

        Dado una ciudad y un año obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en ese año dividido por meses
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadPorcentajelPernoctacionesEnCiudadEnAnioMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en esos años
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadPorcentajePernoctacionesEnCiudadEnRangoAnios/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_rango_anios_en_mes

        Dado una ciudad, un mes y un rango de años obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en esos años en ese mes dando
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadPorcentajePernoctacionesEnCiudadEnRangoAniosEnMes/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_pernoctaciones_en_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_pernoctaciones_en_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que pernoctan en dicha ciudad en ese año
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadTotalPernoctacionesEnCiudadEnAnio/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_pernoctaciones_en_ciudad_en_anio_mensualmente dividido por meses(self):
        """
        Test case for obtener_cantidad_total_pernoctaciones_en_ciudad_en_anio_mensualmente dividido por meses

        Dado una ciudad y un año obtiene la cantidad total de personas que pernoctan en dicha ciudad en ese año dividido por meses
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadTotalPernoctacionesEnCiudadEnAnioMensualmente/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_pernoctaciones_en_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_total_pernoctaciones_en_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que pernoctan en dicha ciudad en esos años
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadTotalPernoctacionesEnCiudadEnRangoAnios/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_pernoctaciones_en_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_total_pernoctaciones_en_ciudad_en_rango_anios_en_mes

        Dado una ciudad, un mes y un rango de años obtiene la cantidad total de personas que pernoctan en dicha ciudad en esos años en ese mes
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Pernotaciones/ObtenerCantidadTotalPernoctacionesEnCiudadEnRangoAniosEnMes/{Ciudad}'.format(Ciudad='Ciudad_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
