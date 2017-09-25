import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_anio_mensualmente(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios_en_mes(CiudadOrigen, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_en_rango_anios_mensualmente(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese rango de años
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese rango de años
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante un rango de años de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_anio(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
    Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_anio_mensualmente(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad de personas que van a apartamentos turisticos de esa ciudad de forma mensual
    Dado una ciudad y un año obtiene la cantidad de personas que van a apartamentos turisticos de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios(CiudadDestino, Anio):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios_en_mes(CiudadDestino, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios_mensualmente(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_en_anio_mensualmente(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios_en_mes(CiudadOrigen, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_en_rango_anios_mensualmente(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_anio(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese año
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese año
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese rango de años
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante ese rango de años
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a campings de la ciudad destino desde la ciudad origen durante un rango de años de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_hacia_ciudad_en_anio(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a campings de esa ciudad
    Dado una ciudad y un año obtiene la cantidad total de personas que van a campings de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_hacia_ciudad_en_anio_mensualmente(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad de personas que van a campings de esa ciudad de forma mensual
    Dado una ciudad y un año obtiene la cantidad de personas que van a campings de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios(CiudadDestino, Anio):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios_en_mes(CiudadDestino, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios_mensualmente(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_en_anio_mensualmente(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios_en_mes(CiudadOrigen, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_en_rango_anios_mensualmente(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_anio(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese año
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese año
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese rango de años
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante ese rango de años
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a hoteles de la ciudad destino desde la ciudad origen durante un rango de años de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_hacia_ciudad_en_anio(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles de esa ciudad
    Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_hacia_ciudad_en_anio_mensualmente(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad de personas que van a hoteles de esa ciudad de forma mensual
    Dado una ciudad y un año obtiene la cantidad de personas que van a hoteles de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios(CiudadDestino, Anio):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios_en_mes(CiudadDestino, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios_mensualmente(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_en_anio_mensualmente(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios_en_mes(CiudadOrigen, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_en_rango_anios_mensualmente(CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_anio(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese año
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese año
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese año de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese rango de años
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante ese rango de años
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    Dado una ciudad origen, una ciudad destino, un mes y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante un rango de años durante un mes
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_mensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante un rango de años  de forma mensual
    Dado una ciudad origen, una ciudad destino y un rango de años obtiene la cantidad total de personas que van a residencias de la ciudad destino desde la ciudad origen durante un rango de años de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_hacia_ciudad_en_anio(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias de esa ciudad
    Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_hacia_ciudad_en_anio_mensualmente(CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad de personas que van a residencias de esa ciudad de forma mensual
    Dado una ciudad y un año obtiene la cantidad de personas que van a residencias de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios(CiudadDestino, Anio):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios_en_mes(CiudadDestino, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios_mensualmente(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad de forma mensual
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad de forma mensual
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param AnioInicio: Anio inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_total_personas_en_apartamentos_turisticos_desde_ciudad_en_anio(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a apartamentos turisticos desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_total_personas_en_camping_desde_ciudad_en_anio(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a campings desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_total_personas_en_hotel_desde_ciudad_en_anio(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a hoteles desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'


def obtener_cantidad_total_personas_en_residencias_desde_ciudad_en_anio(CiudadOrigen, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que van a residencias desde esa ciudad de forma total
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    return 'do some magic!'
