from ..DB.Repositorio_Grado_De_Ocupacion_Apartamentos_INE import RepositoryGradoOcupacionApartamentosINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor

def obtener_porcentaje_del_grado_de_ocupacion_por_apartamentos_en_ciudad_en_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene el porcentaje del grado de ocupación por apartamentos  en dicha ciudad en ese año
    Dado una ciudad y un año obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en ese año
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnio(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_porcentaje_del_grado_de_ocupacion_por_apartamentos_en_ciudad_en_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en ese año dividido por meses
    Dado una ciudad y un año obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en ese año dividido por meses
    :param Ciudad: Ciudad
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_porcentaje_del_grado_de_ocupacion_por_apartamentos_en_ciudad_en_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en esos años
    Dado una ciudad y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en esos años
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

    cursor, labels = repository.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval
#PONER EN SWAGGER
    
def obtener_porcentaje_del_grado_de_ocupacion_por_apartamentos_en_ciudad_en_rango_anios_mensualmente(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en esos años mensualmente
    Dado una ciudad y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en esos años mensualmente
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

    cursor, labels = repository.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosMensualmente(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_porcentaje_del_grado_de_ocupacion_por_apartamentos_en_ciudad_en_rango_anios_en_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un mes y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en esos años en ese mes
    Dado una ciudad, un mes y un rango de años obtiene el porcentaje del grado de ocupación por apartamentos en dicha ciudad en esos años en ese mes
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

    cursor, labels = repository.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval
