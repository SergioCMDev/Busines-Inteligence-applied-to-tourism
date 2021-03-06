from ..DB.Repositorio_Turistas_Salientes_INE import RepositoryTuristasSalientesINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_porcentaje_total_turistas_salientes_de_ciudad_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad de forma total durante ese año
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad de forma total durante ese año
    :param Ciudad: Ciudad origen
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnio(Ciudad, Anio)
                    
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval




def obtener_porcentaje_turistas_salientes_de_ciudad_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad de forma total durante ese año de forma mensual
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad de forma total durante ese año de forma mensual
    :param Ciudad: Ciudad origen
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_porcentaje_turistas_salientes_de_ciudad_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que salen de esa ciudad de forma total durante esos años
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que salen de esa ciudad de forma total durante esos años
    :param Ciudad: Ciudad origen
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Finobtener_cantidad_total_turistas_salientes_de_ciudad_anio
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_porcentaje_turistas_salientes_de_ciudad_rango_anios_mensualmente(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que salen de esa ciudad de forma total durante esos años 
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que salen de esa ciudad de forma total durante esos años mensualmente
    :param Ciudad: Ciudad origen
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosMensualmente(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_porcentaje_turistas_salientes_de_ciudad_rango_anios_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que salen de esa ciudad de forma global durante esos años en ese mismo mes
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que salen de esa ciudad de forma global durante esos años en ese mismo mes
    :param Ciudad: Ciudad origen
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

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_porcentaje_turistas_salientes_de_ciudad_origen_hacia_ciudad_destino_en_rango_anio_mensualmente(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param CiudadOrigen: Ciudad Origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosMensualmente(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_porcentaje_turistas_salientes_de_ciudad_origen_hacia_ciudad_destino_en_rango_anios(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param CiudadOrigen: Ciudad Origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAnios(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_porcentaje_turistas_salientes_de_ciudad_origen_hacia_ciudad_destino_en_anio(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante ese año de forma anual
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante ese año de forma anual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval



    	
def obtener_porcentaje_turistas_salientes_de_ciudad_origen_hacia_ciudad_destino_en_anio_mensualmente(CiudadOrigen, CiudadDestino, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad y van hacia ciudad destino de forma total durante ese año de forma mensual
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad y van hacia ciudad destino de forma total durante ese año de forma mensual
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval





def obtener_porcentaje_turistas_salientes_de_ciudad_origen_hacia_ciudad_destino_en_rango_anio_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad y van hacia ciudad destino de forma total durante esos años de forma anual durante ese mes
    Dado una ciudad y un año obtiene la cantidad total de personas que salen de esa ciudad y van hacia ciudad destino de forma total durante esos años de forma anual durante ese mes
    :param CiudadOrigen: Ciudad origen
    :type CiudadOrigen: str
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFIn: Anio Fin
    :type AnioFIn: int
    :param Mes: Mes
    :type Mes: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval





