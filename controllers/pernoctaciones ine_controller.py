from ..DB.Repositorio_Pernoctaciones_INE import RepositoryPernoctacionesINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor



def obtener_cantidad_personas_en_apartamentos_turisticos_desde_ciudad_origen_hacia_ciudad_destino_en_anio(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese año
    Dado una ciudad origen, una ciudad destino, un año obtiene la cantidad total de personas que van a apartamentos turisticos de la ciudad destino desde la ciudad origen durante ese año
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(CiudadOrigen,CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en ese año
    Dado una ciudad y un año obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en ese año
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajePernoctacionesEnCiudadEnAnio(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en ese año dividido por meses
    Dado una ciudad y un año obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en ese año dividido por meses
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajePernoctacionesEnCiudadEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en esos años
    Dado una ciudad y un rango de años obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en esos años
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Año Inicio
    :type AnioInicio: int
    :param AnioFin: Año Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajePernoctacionesEnCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_porcentaje_pernoctaciones_en_ciudad_en_rango_anios_en_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un mes y un rango de años obtiene el tanto por ciento de la cantidad total de personas que pernoctan en dicha ciudad en esos años en ese mes dando
    Dado una ciudad, un mes y un rango de años obtiene el tanto por ciento  la cantidad total de personas que pernoctan en dicha ciudad en esos años en ese mes
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Año Inicio
    :type AnioInicio: int
    :param AnioFin: Año Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajePernoctacionesEnCiudadEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_total_pernoctaciones_en_ciudad_en_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que pernoctan en dicha ciudad en ese año
    Dado una ciudad y un año obtiene la cantidad total de personas que pernoctan en dicha ciudad en ese año
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalPernoctacionesEnAnio(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_total_pernoctaciones_en_ciudad_en_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que pernoctan en dicha ciudad en ese año dividido por meses
    Dado una ciudad y un año obtiene la cantidad total de personas que pernoctan en dicha ciudad en ese año dividido por meses
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalPernoctacionesEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_total_pernoctaciones_en_ciudad_en_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que pernoctan en dicha ciudad en esos años
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que pernoctan en dicha ciudad en esos años
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalPernoctacionesEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_total_pernoctaciones_en_ciudad_en_rango_anios_en_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un mes y un rango de años obtiene la cantidad total de personas que pernoctan en dicha ciudad en esos años en ese mes
    Dado una ciudad, un mes y un rango de años obtiene la cantidad total de personas que pernoctan en dicha ciudad en esos años en ese mes
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadTotalPernoctacionesEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval