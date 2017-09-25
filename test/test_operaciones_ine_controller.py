# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestOperacionesINEController(BaseTestCase):
    """ OperacionesINEController integration test stubs """

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese año de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese rango de años
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes

        Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnApartamentosTuristicosHaciaCiudadEnAnio/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad de personas que van a apartamentos turisticos de esa ciudad de forma mensual
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosHaciaCiudadEnAnioMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosHaciaCiudadEnRangoAnios/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosHaciaCiudadEnRangoAniosEnMes/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnApartamentosTuristicosHaciaCiudadEnRangoAniosMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnDesdeCiudadEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_anio

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese año
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese año de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese rango de años
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes

        Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_hacia_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_camping_hacia_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a campings de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnCampingHaciaCiudadEnAnio/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_hacia_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_camping_hacia_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad de personas que van a campings de esa ciudad de forma mensual
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingHaciaCiudadEnAnioMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingHaciaCiudadEnRangoAnios/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingHaciaCiudadEnRangoAniosEnMes/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnCampingHaciaCiudadEnRangoAniosMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_anio

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese año
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnHotelDesdeCiudadOrigenHaciaCiudadDestinoEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese año de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese rango de años
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes

        Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_hacia_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_hacia_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnHotelHaciaCiudadEnAnio/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_hacia_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_hacia_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad de personas que van a hoteles de esa ciudad de forma mensual
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelHaciaCiudadEnAnioMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelHaciaCiudadEnRangoAnios/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelHaciaCiudadEnRangoAniosEnMes/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnHotelHaciaCiudadEnRangoAniosMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_anio

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese año
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnResidenciaDesdeCiudadOrigenHaciaCiudadDestinoEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente

        Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese año de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese rango de años
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes

        Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente

        Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
        """
        query_string = [('CiudadDestino', 'Málaga'),
                        ('AnioInicio', 2002),
                        ('AnioFin', 2004)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_hacia_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_hacia_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnResidenciaHaciaCiudadEnAnio/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_hacia_ciudad_en_anio_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_hacia_ciudad_en_anio_mensualmente

        Dado una ciudad y un año obtiene la cantidad de personas que van a residencias de esa ciudad de forma mensual
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaHaciaCiudadEnAnioMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaHaciaCiudadEnRangoAnios/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios_en_mes(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios_en_mes

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002),
                        ('Mes', 'Enero')]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaHaciaCiudadEnRangoAniosEnMes/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios_mensualmente(self):
        """
        Test case for obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios_mensualmente

        Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad de forma mensual
        """
        query_string = [('AnioInicio', 2002),
                        ('AnioFin', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadPersonasEnResidenciaHaciaCiudadEnRangoAniosMensualmente/{CiudadDestino}'.format(CiudadDestino='CiudadDestino_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_personas_en_apartamentos_turisticos_desde_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_personas_en_apartamentos_turisticos_desde_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnApartamentosTuristicosDesdeCiudadEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_personas_en_camping_desde_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_personas_en_camping_desde_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnCampingDesdeCiudadEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_personas_en_hotel_desde_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_personas_en_hotel_desde_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnHotelDesdeCiudadEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_obtener_cantidad_total_personas_en_residencias_desde_ciudad_en_anio(self):
        """
        Test case for obtener_cantidad_total_personas_en_residencias_desde_ciudad_en_anio

        Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
        """
        query_string = [('Anio', 2002)]
        response = self.client.open('/server/INE/Operaciones/ObtenerCantidadTotalPersonasEnResidenciaDesdeCiudadEnAnio/{CiudadOrigen}'.format(CiudadOrigen='CiudadOrigen_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
