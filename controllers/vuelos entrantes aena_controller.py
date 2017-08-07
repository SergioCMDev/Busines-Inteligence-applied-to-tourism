from ..DB.DBRepositoryAena import DBRepositoryAena as DBRepository
from ..Utilidades.Conversores import Conversores as Conversor


def obtener_cantidad_anio_ciudad(PaisDestino, CiudadDestino, Anio): #OK
    """
    Obtener cantidades de vuelos entrantes en la ciudad del pais divididas por meses
    Obtener cantidad de vuelos entrantes en las ciudades de un pais de divididas por meses
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(PaisDestino, CiudadDestino, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)
#    print(arrayTuplas)
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)

#    return retval

    ##Mostrar JSON Reducido
    retval = conversor.convertirAJson(arrayTuplas)
    return retval

    




def obtener_cantidad_anio_por_ciudades(PaisDestino, Anio):
    """
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(PaisDestino, Anio)
    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)
    
    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval

#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_anualmente(PaisDestino, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes anualmente dado un pais destino y un rango de años
    Obtiene la cantidad total de vuelos entrantes de cada año
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval

#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_ciudad(PaisDestino, CiudadDestino, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes en una ciudad de un pais durante el rango de años seleccionado
    Obtener cantidad de vuelos entrantes totales en las ciudades de un pais durante un rango de años
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
    

def obtener_cantidad_entrantes_por_ciudades(PaisDestino, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_mensual(PaisDestino, Anio):
    """
    Obtener cantidad de vuelos entrantes durante los meses de un año 
    Obtiene la cantidad de vuelos totales de cada mes durante un año seleccionado
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(PaisDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_mensualmente(PaisDestino, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes de forma mensual dado un pais destino y un rango de años
    Obtiene la cantidad de vuelos en cada mes durante los años seleccionados
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_mes(PaisDestino, Mes, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes durante el mismo mes en un rango de años para el pais destino
    Obtiene la cantidad de vuelos en un mes durante los años seleccionados
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Mes: Mes
    :type Mes: str
    :param AnioInicio: Año Inicio
    :type AnioInicio: int
    :param AnioFin: Año Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(PaisDestino, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)
    
    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_mes_anio_por_ciudades(PaisDestino, Anio, Mes):
    """
    Obtener cantidad de vuelos entrantes en las ciudades del pais durante el mes del año seleccionado
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int
    :param Mes: Mes
    :type Mes: str

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(PaisDestino, Mes, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_cantidad_mes_ciudad(PaisDestino, CiudadDestino, Mes, AnioInicio, AnioFin):
    """
    Obtener cantidad de vuelos entrantes en la ciudad del pais durante el mes del rango de años seleccionado
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un año
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param CiudadDestino: Ciudad a la que llegan los vuelos
    :type CiudadDestino: str
    :param Mes: Mes
    :type Mes: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: None
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval



def obtener_cantidad_mes_por_ciudades(PaisDestino, AnioInicio, AnioFin, Mes):
    """
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años durante un mismo mes
    Obtener cantidad de vuelos entrantes en las ciudades de un pais durante un rango de años durante el mismo
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
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

    cursor, labels = repository.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(PaisDestino, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)


    ##Mostrar JSON Extendido
    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
    retval = conversor.ObtenerDataJSONExtendido(matriz)
    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
    
#TODO

def obtener_paises_origen_ciudad_origen_y_cantidad_anualmente(PaisDestino, AnioInicio, AnioFin): #TODo
    """
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino y rango de años
    Obtiene la cantidad total de vuelos entrantes a un pais y los paises origen durante un rango de años 
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval
    


def obtener_paises_origen_ciudad_origen_y_cantidad_anualmente_en_mes(PaisDestino, Mes, AnioInicio, AnioFin): #TODO
    """
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino, un rango de años y un mes
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino, un rango de años y un mes
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Mes: Mes a filtrar
    :type Mes: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoMesAnioMinMax(PaisDestino, Mes, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_paises_origen_ciudad_origen_y_cantidad_en_anio(PaisDestino, Anio): #TODO
    """
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino y un año
    Obtiene la cantidad total de vuelos entrantes de cada 
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesDuranteAnioAenaDadoPaisDestinoAnio(PaisDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_paises_origen_y_cantidad_anualmente(PaisDestino, AnioInicio, AnioFin): #TODo
    """
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino y rango de años
    Obtiene la cantidad total de vuelos entrantes a un pais y los paises origen durante un rango de años 
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param AnioInicio: Anio Inicio
    :type AnioInicio: int
    :param AnioFin: Anio Fin
    :type AnioFin: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisesOrigenYVuelosEntrantesDuranteAniosAenaDadoPaisDestinoAnioMinMax(PaisDestino, AnioInicio, AnioFin)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_paises_origen_y_cantidad_en_anio(PaisDestino, Anio): #TODO
    """
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino y un año
    Obtiene la cantidad total de vuelos entrantes de cada 
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYVuelosEntrantesAenaDadoPaisDestinoAnio(PaisDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_paises_origen_y_cantidad_en_ciudad_y_anio(PaisDestino, ciudadDestino, Anio):  #TODO
    """
    Obtener cantidad de vuelos entrantes y los paises de origen anualmente dado un pais destino y un año
    Obtiene la cantidad total de vuelos entrantes de cada 
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param ciudadDestino: Ciudad a la que llegan los vuelos
    :type ciudadDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisOrigenYVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnio(PaisDestino, ciudadDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


def obtener_paises_origen_y_cantidad_mensualmente_en_anio(PaisDestino, Anio):#TODO
    """
    Obtener cantidad de vuelos entrantes y los paises de origen durante un año separando por meses dado un pais destino y un año
    Obtiene la cantidad total de vuelos entrantes de cada 
    :param PaisDestino: Pais al que llegan los vuelos
    :type PaisDestino: str
    :param Anio: Anio
    :type Anio: int

    :rtype: Dict[str, int]
    """
    conversor = Conversor()
    repository = DBRepository()

    cursor, labels = repository.ObtenerPaisesOrigenYVuelosEntrantesMensualmenteDuranteAniosAenaDadoPaisDestinoAnio(PaisDestino, Anio)

    arrayTuplas =  conversor.ConvertirCursorToTuplas(cursor)

###TEST
    ##Mostrar JSON Extendido
#    matriz, lista = conversor.ConvertirTuplasToMatriz(arrayTuplas,  labels)
#    retval = conversor.ObtenerDataJSONExtendido(matriz)
#    return retval


#    #Mostrar JSON Reducido
#    retval = conversor.convertirAJson(arrayTuplas)
#    return retval


