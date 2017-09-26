from ..DB.Repositorio_Turistas_Entrantes_INE import RepositoryTuristasEntrantesINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_cantidad_turistas_entrantes_en_ciudad_destino_desde_ciudad_origen_en_rango_anio_mensualmente(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan a esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan a esa ciudad de forma total
    :param Ciudad: Ciudad destino
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_total_turistas_entrantes_en_ciudad_anio(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan a esa ciudad de forma total
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan a esa ciudad de forma total
    :param Ciudad: Ciudad destino
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnio(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_turistas_entrantes_de_ciudad_origen_hacia_ciudad_destino_en_rango_anio_en_mes(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual durante ese mes
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual durante ese mes
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param CiudadOrigen: Ciudad Origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosEnMes(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_turistas_entrantes_en_ciudad_anio_mensualmente(Ciudad, Anio):
    """
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante los meses de ese año
    Dado una ciudad y un año obtiene la cantidad total de personas que llegan a esa ciudad de forma global durante los meses de ese año
    :param Ciudad: Ciudad destino
    :type Ciudad: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnioMensualmente(Ciudad, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_turistas_entrantes_en_ciudad_destino_desde_ciudad_origen_en_anio(CiudadDestino, CiudadOrigen, Anio):
    """
    Dado una ciudad destino, una ciudad origen y un año obtiene la cantidad total de personas que llegan a ciudad Destino desde ciudad origen durante ese año de forma anual
    Dado una ciudad destino, una ciudad origen y un año obtiene la cantidad total de personas que llegan a ciudad Destino desde ciudad origen durante ese año de forma anual
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param CiudadOrigen: Ciudad Origen
    :type CiudadOrigen: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnAnio(CiudadDestino, CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_turistas_entrantes_en_ciudad_destino_desde_ciudad_origen_en_rango_anio_en_mes(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad destino, una ciudad origen, un mes y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual durante ese mes
    Dado una ciudad destino, una ciudad origen, un mes y un año obtiene la cantidad total de personas que salen de ciudad origen y van hacia ciudad destino de forma total durante esos años de forma anual durante ese mes
    :param CiudadDestino: Ciudad Destino
    :type CiudadDestino: str
    :param CiudadOrigen: Ciudad Origen
    :type CiudadOrigen: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int
    :param Mes: Mes
    :type Mes: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosEnMes(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_turistas_entrantes_en_ciudad_destino_desde_ciudad_origen_en_rango_anios(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
    """
    Dado una ciudad destino, una ciudad origen y un rango de años obtiene la cantidad total de personas que llegan a ciudad destino desde ciudad origen durante esos años de forma anual
    Dado una ciudad destino, una ciudad origen y un rango de años obtiene la cantidad total de personas que llegan a ciudad destino desde ciudad origen durante esos años de forma anual
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

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAnios(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval
def obtener_cantidad_turistas_entrantes_en_ciudad_rango_anios(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante esos años
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante esos años
    :param Ciudad: Ciudad destino
    :type Ciudad: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAnios(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


def obtener_cantidad_turistas_entrantes_en_ciudad_rango_anios_en_mes(Ciudad, AnioInicio, AnioFin, Mes):
    """
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante esos años durante ese mes
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante esos años durante ese mes
    :param Ciudad: Ciudad destino
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

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosEnMes(Ciudad, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_turistas_entrantes_en_ciudad_rango_anios_mensualmente(Ciudad, AnioInicio, AnioFin):
    """
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante esos años separados por meses
    Dado una ciudad, un rango de años y un mes obtiene la cantidad total de personas que llegan a esa ciudad de forma total durante esos años separados por meses
    :param Ciudad: Ciudad destino
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

    cursor, labels = repository.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosMensualmente(Ciudad, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

obtener_cantidad_turistas_entrantes_en_ciudad_destino_desde_ciudad_origen_en_rango_anio_mensualmente