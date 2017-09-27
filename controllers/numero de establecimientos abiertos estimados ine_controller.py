from ..DB.Repositorio_Numero_De_Establecimientos_Abiertos_Estimados_INE import RepositoryNumeroEstablecimientosAbiertosEstimadosINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_numero_de_establecimientos_abiertos_estimados_en_ciudad_en_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene el numero de establecimientos abiertos estimados en dicha ciudad en ese año
    Dado una ciudad y un año obtiene el numero de establecimientos abiertos estimados en dicha ciudad en ese año
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnio(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_numero_de_establecimientos_abiertos_estimados_en_ciudad_en_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene el numero de establecimientos abiertos estimados en dicha ciudad en ese año dividido por meses
    Dado una ciudad y un año obtiene el numero de establecimientos abiertos estimados en dicha ciudad en ese año dividido por meses
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_numero_de_establecimientos_abiertos_estimados_en_ciudad_en_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene el numero de establecimientos abiertos estimados en dicha ciudad en esos años
    Dado una ciudad y un rango de años obtiene el numero de establecimientos abiertos estimados en dicha ciudad en esos años
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

    cursor, labels = repository.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_numero_de_establecimientos_abiertos_estimados_en_ciudad_en_rango_anios_mensualmente(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene el numero de establecimientos abiertos estimados en dicha ciudad en esos años mensualmente
    Dado una ciudad y un rango de años obtiene el numero de establecimientos abiertos estimados en dicha ciudad en esos años mensualmente
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

    cursor, labels = repository.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_numero_de_establecimientos_abiertos_estimados_en_ciudad_en_rango_anios_en_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un mes y un rango de años obtiene el numero de establecimientos abiertos estimados en dicha ciudad en esos años en ese mes
    Dado una ciudad, un mes y un rango de años obtiene el numero de establecimientos abiertos estimados en dicha ciudad en esos años en ese mes
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

    cursor, labels = repository.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval