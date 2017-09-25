import connexion
from swagger_server.models.body1 import Body1
from swagger_server.models.body2 import Body2
from swagger_server.models.body3 import Body3
from swagger_server.models.body4 import Body4
from swagger_server.models.body5 import Body5
from swagger_server.models.body6 import Body6
from swagger_server.models.body7 import Body7

from ..Utilidades.UtilidadesTensorFlow import UtilidadesTensorFlow as Tensorflow
tensorflow = Tensorflow()
from ..Utilidades.Conversores import Conversores 
conversor = Conversores()
from ..Utilidades.DeteccionOutliers import DeteccionOutliers
outliers = DeteccionOutliers()
from ..Utilidades.Graphics import Graphics as Graphics
graphics = Graphics()



def obtener_outliers_ciudad_cantidad(ciudadInicioIniciales, CiudadFinIniciales, Metodo, body): #OK
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales  y unos valores a tratar
    Este metodo trata los valores de cada mes de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param ciudadInicioIniciales: Ciudad inicial de la matriz de datos
    :type ciudadInicioIniciales: str
    :param CiudadFinIniciales: Ciudad final de la matriz de datos, las siguientes se probaran mediante los metodos de deteccion de outliers
    :type CiudadFinIniciales: str
    :param Metodo: Metodo a usar para obtener los outliers
    :type Metodo: str
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body5.from_dict(d) for d in connexion.request.get_json()]
        listaLabels = list()
        listaLabels.append('Ciudad')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, CiudadFinIniciales)
#        print(listaValores)
#        print("\n")
#        print(listaValoresAComprobar)
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)
#        print(matriz)
#        print("\n")
#        print(listaColumnas)
        
        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, ciudadInicioIniciales, CiudadFinIniciales, listaValoresAComprobar, listaLabels, Metodo)
#        print(listaValoresOutliers)
#        print("\n")
#        print(listaValoresInliers)
    
#        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, ciudadInicioIniciales, CiudadFinIniciales, listaValoresAComprobar, listaLabels, listaColumnas)
#        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, ciudadInicioIniciales, CiudadFinIniciales, listaValoresAComprobar, listaLabels, listaColumnas)
        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)
        #OK








"""
"[{\"Anio\":2009,\"Numero_Vuelos\":209861},{\"Anio\":2010,\"Numero_Vuelos\":208851},{\"Anio\":2011,\"Numero_Vuelos\":205476},{\"Anio\":2012,\"Numero_Vuelos\":130233},{\"Anio\":2013,\"Numero_Vuelos\":121931},{\"Anio\":2014,\"Numero_Vuelos\":126893},{\"Anio\":2015,\"Numero_Vuelos\":139735}]"
"""
def obtener_outliers_inliers_anios_cantidad(AnioInicio, AnioFin, Metodo,  body): #OK
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    :param AnioInicio: Año inicial de la matriz de datos
    :type AnioInicio: str
    :param AnioFin: Año final de la matriz de datos,  Año final de la matriz de datos, año desde el cual obtenemos los datos a probar
    :type AnioFin: str
    :param Metodo: Metodo a usar para obtener los outliers
    :type Metodo: str
    :param body: Datos de entrada obtenidos previamente
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body.from_dict(d) for d in connexion.request.get_json()]

        listaLabels = list()
        listaLabels.append('Anio')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, AnioFin)


#        print(listaValoresAComprobar)
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)
#        print(matriz)
        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, Metodo)
        
        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaColumnas)


        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)


        
#        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaColumnas)
#        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaColumnas)
#OK


def obtener_outliers_pais_cantidad(PaisInicioIniciales, PaisFinIniciales, Metodo, body): #OK
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales  y unos valores a tratar
    Este metodo trata los valores de cada mes de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param PaisInicioIniciales: Pais inicial de la matriz de datos
    :type PaisInicioIniciales: str
    :param AnioFin: Pais final de la matriz de datos, los datos siguientes se trataran mediante los metodos de deteccion de outliers
    :type AnioFin: str
    :param Metodo: Metodo a usar para obtener los outliers
    :type Metodo: str
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body6.from_dict(d) for d in connexion.request.get_json()]
        listaLabels = list()
        listaLabels.append('Pais')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, PaisFinIniciales)
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)

        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, PaisInicioIniciales, PaisFinIniciales, listaValoresAComprobar, listaLabels, Metodo)
#        print(listaValoresOutliers)
#        print("\n")
#        print(listaValoresInliers)

        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, PaisInicioIniciales, PaisFinIniciales, listaValoresAComprobar, listaLabels, listaColumnas)
        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, PaisInicioIniciales, PaisFinIniciales, listaValoresAComprobar, listaLabels, listaColumnas)

            
        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)
       #OK
 
        
def obtener_outliers_inliers_mes_cantidad(MesInicioIniciales, MesFinIniciales, Metodo, body): #OK
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales  y unos valores a tratar
    Este metodo trata los valores de cada mes de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param MesInicio: Mes inicial de la matriz de datos
    :type MesInicio: str
    :param AnioFin: Mes final de la matriz de datos, los siguientes se probaran mediante los metodos de deteccion de outliers
    :type AnioFin: str
    :param Metodo: Metodo a usar para obtener los outliers
    :type Metodo: str
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body4.from_dict(d) for d in connexion.request.get_json()]
        listaLabels = list()
        listaLabels.append('Mes')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, MesFinIniciales)
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)
       
        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, MesInicioIniciales, MesFinIniciales, listaValoresAComprobar, listaLabels, Metodo)
#        print(listaValoresOutliers)
#        print("\n")
#        print(listaValoresInliers)    
#        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, MesInicioIniciales, MesFinIniciales, listaValoresAComprobar, listaLabels, listaColumnas)
#        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, MesInicioIniciales, MesFinIniciales, listaValoresAComprobar, listaLabels, listaColumnas)
        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)
#        OK





def obtener_outliers_inliers_anios_pais_cantidad(AnioInicio, AnioFin, Metodo, body):#OK
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    Este metodo trata los valores de cada mes de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param AnioInicio: Año inicial de la matriz de datos
    :type AnioInicio: int
    :param AnioFin: Año final de la matriz de datos, a partir de este año comienan los datos de prueba
    :type AnioFin: int
    :param Metodo: Metodo a usar para obtener los outliers
    :type Metodo: str
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body2.from_dict(d) for d in connexion.request.get_json()]
        listaLabels = list()
        listaLabels.append('Anio')
        listaLabels.append('Pais')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, AnioFin)
#        print( listaValores)
#        print("\n")
#        print(listaValoresAComprobar)
#        print("\n")
#        print(listaValoresCentrales)
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)
        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, Metodo)
#        print(listaColumnas)
#        print(listaValoresOutliers)
#        print("\n")
#        print(listaValoresInliers)         
#        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaValoresCentrales)
#        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaValoresCentrales)
        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)
#        OK



def obtener_outliers_inliers_anios_mes_cantidad(AnioInicio, AnioFin, Metodo,  body): #OK
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales y unos valores a tratar
    Este metodo trata los valores de cada mes de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param AnioInicio: Año inicial de la matriz de datos
    :type AnioInicio: int
    :param AnioFin: Año final de la matriz de datos
    :type AnioFin: int
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """

    if connexion.request.is_json:
        body = [Body1.from_dict(d) for d in connexion.request.get_json()]
        listaLabels = list()
        listaLabels.append('Anio')
        listaLabels.append('Mes')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, AnioFin)

        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)
#        print(matriz)
        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, Metodo)

#        print(listaValoresOutliers)
#        print("\n")
#
#        print(listaValoresInliers)
#        
        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin,listaValoresAComprobar, listaLabels, listaColumnas)
        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, AnioInicio, AnioFin,listaValoresAComprobar, listaLabels, listaColumnas)

        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)
        #OK

def obtener_outliers_inliers_anios_ciudad_cantidad(AnioInicio, AnioFin, Metodo,  body): 
    """
    Obtener los valores fuera de lo comun dado unos valores iniciales  y unos valores a tratar
    Este metodo trata los valores de cada ciudad de cada año y tras pasarle valores a probar decide los inliers y los outliers
    :param AnioInicio: Año inicial de la matriz de datos
    :type AnioInicio: int
    :param AnioFin: Año final de la matriz de datos, año a partir del cual obtenemos los datos a probar
    :type AnioFin: int
    :param Metodo: Metodo a usar para obtener los outliers
    :type Metodo: str
    :param body: Datos de entrada obtenidos previamente junto con los datos a testear
    :type body: list | bytes

    :rtype: Dict[str, int]
    """
    if connexion.request.is_json:
        body = [Body3.from_dict(d) for d in connexion.request.get_json()]
#        print(body)
        listaLabels = list()
        listaLabels.append('Anio')
        listaLabels.append('Ciudad')
        listaLabels.append('Cantidad')
        listaValores, listaValoresAComprobar, listaValoresCentrales = conversor.separarValoresBody(body, AnioFin)
#        print( listaValores)
#        print("\n")
#        print(listaValoresAComprobar)
#        print("\n")
#        print(listaValoresCentrales)
#OK
        matriz, listaColumnas =  conversor.ConvertirTuplasToMatriz(listaValores, listaLabels)
#        print(listaColumnas)
        listaValoresOutliers, listaValoresInliers = outliers.ObtenerOutliersDadaMatrizAniosYTipo(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, Metodo)
        
#        print(listaValoresOutliers)
#        print("\n")
#        print(listaValoresInliers)
            
            #TODO REALIZAR AMBAS GRAFICAS
#        print(listaColumnas)
#        outliers.MostrarOutliersMedianteEnvolturaElipticaDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaValoresCentrales)
#        outliers.MostrarOutliersMedianteIsolationForestDadosDatos(matriz, AnioInicio, AnioFin, listaValoresAComprobar, listaLabels, listaValoresCentrales)
#        print(listaValoresOutliers)
#        print(listaValoresCentrales)


        return conversor.ObtenerJSONDeListasOutliersInliers(listaValoresInliers, listaValoresOutliers, listaLabels, listaValoresCentrales)
        #OK

"""
    Probar en postman con entrada [{"Anio": 2009,"Cantidad": 46453}, {"Anio": 2010,"Cantidad": 44721}, {"Anio": 2011,"Cantidad": 61420}]
"""
def obtener_progresion_lineal(AnioPrediccion, body):

#def obtener_progresion_lineal_anio_cantidad(AnioPrediccion, body):
    """
    Obtener la prediccion para un año dado el año a predecir y los datos de varios años anteriores
    Obtener la prediccion para un año dado el año a predecir y los datos de varios años anteriores
    :param AnioPrediccion: Año para predecir la cantidad
    :type AnioPrediccion: str
    :param body: Datos de entrada obtenidos previamente
    :type body: list | bytes

    :rtype: int
    """
    prediccionCantidad = -1
    if connexion.request.is_json:
        body = [Body7.from_dict(d) for d in connexion.request.get_json()]
        lista = list()
        
        print(body)
        for item in body:
            if(hasattr(item, 'anio') and hasattr(item, 'cantidad')):
                tupla = (item.anio, item.cantidad)
            lista.append(tupla)
        prediccionCantidad = tensorflow.ObtenerProgresionLineal(lista, int(AnioPrediccion))

    return int(prediccionCantidad)



