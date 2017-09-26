from ..DB.Repositorio_Numero_De_Plazas_Estimadas_INE import RepositoryNumeroPlazasEstimadasINE as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor



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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnAnioMensualmente(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnAnioMensualmente(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAniosEnMes(CiudadOrigen, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_personas_en_camping_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnAnioMensualmente(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAniosEnMes(CiudadOrigen, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAnios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_personas_en_hotel_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadorigenEnAnioMensualmente(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAniosEnMes(CiudadOrigen, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadOrigen, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

def obtener_cantidad_personas_en_residencias_desde_ciudad_origen_hacia_ciudad_destino_en_rango_anios_en_mes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
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
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, AnioInicio, AnioFin)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnAnio(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnAnio(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval


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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasHotelesDesdeCiudadOrigenEnAnio(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval

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
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnAnio(CiudadOrigen, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels, Anio, Anio)
    retval = conversor.ObtenerDataJSONExtendido(matriz)

    return retval
