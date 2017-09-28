from ..DB.Repositorio_Operaciones_INE import RepositoryOperacionesINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor



################################################################################################################################################################################
###############################################################################        APARTAMENTOS TURISTICOS                ##################################################################
################################################################################################################################################################################

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnio(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    print(matriz)    

    retval = conversor.ObtenerDataJSONExtendido(matriz)
    print(retval)
    return retval

def obtener_cantidad_personas_en_apartamentos_turisticos_hacia_ciudad_en_rango_anios(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a apartamentos turisticos de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


################################################################################################################################################################################
###############################################################################        CAMPING                ##################################################################
################################################################################################################################################################################

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnio(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_personas_en_camping_hacia_ciudad_en_rango_anios(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a campings de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAnios(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

################################################################################################################################################################################
###############################################################################        HOTELES                ##################################################################
################################################################################################################################################################################


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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnio(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_personas_en_hotel_hacia_ciudad_en_rango_anios(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a hoteles de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAnios(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

################################################################################################################################################################################
###############################################################################        RESIDENCIAS                ##################################################################
################################################################################################################################################################################




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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnio(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_personas_en_residencias_hacia_ciudad_en_rango_anios(CiudadDestino, AnioInicio, AnioFin):
    """
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad
    Dado una ciudad y un rango de años obtiene la cantidad total de personas que van a residencias de esa ciudad
    :param CiudadDestino: Ciudad destino
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAnios(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas, labels)

    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval
