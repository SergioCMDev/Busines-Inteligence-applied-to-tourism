# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:10:19 2017

@author: wesrok
"""
from decimal import Decimal
import json
from pandas import DataFrame
from ..Utilidades.UtilidadesMatriz import UtilidadesMatriz as UtilidadesMatriz
from ..Utilidades.Constantes import Constantes

matrix = UtilidadesMatriz()
import numpy
import base64
import numpy as np

class Conversores:   
    def __init__(self):
        print("Clase Conversores Cargada Correctamente ")
        
    @staticmethod
    def default(obj):
        if isinstance(obj, Decimal):
            return str(obj)
        raise TypeError
        
    
    def convertirAJson(self, data):
        retval =  json.dumps(data, default=self.default, separators=(',', ':'))
        return retval 
    
    def convertirNumpyArrayAJson(self, data):

        retval=json.dumps(data,cls=NumpyAwareJSONEncoder)
        return retval 
    
    def separarValoresBody(self, body, ValorFin):
        iniciales = True
        listaValores = list()
        listaValoresCentrales = list()

        listaValoresAComprobar = list()
        buffer = 0
        for item in body:
                    #TODO IR INCREMENTANDO
                if(hasattr(item, 'anio') and hasattr(item, 'pais')  and hasattr(item, 'cantidad')):
                    tupla = (item.anio, item.pais, item.cantidad)
                    if item.pais not in listaValoresCentrales:
                        listaValoresCentrales.append(item.pais)
                    valorItem = item.anio
                    buffer = 1
                elif(hasattr(item, 'anio') and hasattr(item, 'mes')  and hasattr(item, 'cantidad')):
                    tupla = (item.anio, item.mes, item.cantidad)
                    valorItem = item.anio
                    listaValoresCentrales = Constantes.Meses
                    buffer = 1
                elif(hasattr(item, 'anio') and hasattr(item, 'ciudad')  and hasattr(item, 'cantidad')):
                    tupla = (item.anio, item.ciudad, item.cantidad)
                    valorItem = item.anio
                    if item.ciudad not in listaValoresCentrales:
                        listaValoresCentrales.append(item.ciudad)
                    buffer = 1
                elif(hasattr(item, 'anio') and hasattr(item, 'cantidad')):
                    tupla = (item.anio, item.cantidad)
                    valorItem = item.anio
                elif (hasattr(item, 'ciudad') and hasattr(item, 'cantidad')):
                    tupla = (item.ciudad, item.cantidad)
                    if item.ciudad not in listaValoresCentrales:
                        listaValoresCentrales.append(item.ciudad)
                    valorItem = item.ciudad
                elif (hasattr(item, 'pais') and hasattr(item, 'cantidad')):
                    tupla = (item.pais, item.cantidad)
                    if item.pais not in listaValoresCentrales:
                        listaValoresCentrales.append(item.pais)
                    valorItem = item.pais
                elif (hasattr(item, 'mes') and hasattr(item, 'cantidad')):
                    tupla = (item.mes, item.cantidad)
                    listaValoresCentrales = Constantes.Meses

                    valorItem = item.mes
                    
                    
                if iniciales:
                    listaValores.append(tupla)
                else:
                    listaValores.append(tupla)
                    if(valorItem not in listaValoresAComprobar):
                        listaValoresAComprobar.append(valorItem)    
    
                if type(ValorFin) == int:
                    ValorFin = ValorFin + buffer
                if valorItem == ValorFin:
                    iniciales = False
                if type(ValorFin) == int:
                    ValorFin = ValorFin - buffer

        return listaValores, listaValoresAComprobar, listaValoresCentrales
    
    ##Dadas las listas de outliers e inliers y la lista de columnas de la matriz y los valores centrales (para cuando hay tres columnas)
    def ObtenerJSONDeListasOutliersInliers(self, ValoresInliers, ValoresOutliers, listaLabels, listaValoresCentrales):
        print(listaValoresCentrales)
        if len(ValoresOutliers) > 0:
            text = '{"Outliers":['
            for outlier in ValoresOutliers:
                if len(listaLabels) == 3:
                    valorItem = listaLabels[1]
                    item = str(listaValoresCentrales[outlier[0]])
                elif len(listaLabels) == 2  :
                    if( ('Ciudad' in listaLabels[0]  or 'Pais' in listaLabels[0] or 'Mes' in listaLabels[0]) ):
                        valorItem = listaLabels[0]
                        item = str(listaValoresCentrales[outlier[0]])
                    else:
                        valorItem = listaLabels[0]
                        item = str(outlier[0])
                text = text +'{ "'+valorItem+'":' + item  +'},'
            text = text[:-1]
            text = text +']}'
        if len(ValoresInliers) > 0:
            print('dd')
            if len(ValoresOutliers) > 0:    
                text = text[:-1]
                comilla = ','
            else:
                text= "{"
                comilla = ''
                
            text = text + comilla +'"Inliers":['

            for inlier in ValoresInliers:
                if len(listaLabels) == 3:
                    valorItem = listaLabels[1]
                    item = str(listaValoresCentrales[inlier[0]])
                elif len(listaLabels) == 2:
                    if( ('Ciudad' in listaLabels[0]  or 'Pais' in listaLabels[0] or 'Mes' in listaLabels[0]) ):
                        valorItem = listaLabels[0]
                        item = str(listaValoresCentrales[inlier[0]])
                    else:
                        valorItem = listaLabels[0]
                        item = str(inlier[0])
                text = text +'{ "'+valorItem+'": ' + item  +'},'
            text = text[:-1]
            text = text +']}'

        return text
    
    def ObtenerDataJSONExtendido(self, matriz):
        #    print(matriz)
        data = matriz.to_json(orient ='table')
        pos = data.find('"data": ')
        tamRestante = len(data) - pos
        data = data[pos+8 :pos + tamRestante-1]
        return data
    
    def ConvertirCursorToTuplas(self, cursor):
        retVal = list()
        listaCursor = list()
        for elem in cursor.description:
            listaCursor.append(elem[0])
        

        for (listaCursor) in cursor:
            tuples = listaCursor
#            print(tuples)
            retVal.append(tuples)
        
        return retVal


    def ConvertirTuplasToMatriz(self, tuplas, labels):
        print(labels)
        tuplasMatriz = DataFrame(tuplas, columns = labels)
        print("TUPLAS")
        print(tuplasMatriz)
        matriz, lista = matrix.ObtenerMatrizDatos(tuplasMatriz, labels)
#        print(tuplasMatriz)
        return matriz, lista

    def json_numpy_obj_hook(self, dct):
        """Decodes a previously encoded numpy ndarray with proper shape and dtype.
    
        :param dct: (dict) json encoded ndarray
        :return: (ndarray) if input was an encoded ndarray
        """
        if isinstance(dct, dict) and '__ndarray__' in dct:
            data = base64.b64decode(dct['__ndarray__'])
            return np.frombuffer(data, dct['dtype']).reshape(dct['shape'])
        return dct


    def GetComponentesXY(self, lista):
        X_values = []
        Y_values = []
        for pares in lista:
			#print(pares[1])
            X_values.append(int(pares[0]))
            Y_values.append(int(pares[1]))
        return (X_values, Y_values)
    
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        if isinstance(obj, Decimal):
            return str(obj)
        else:
            return super(MyEncoder, self).default(obj)
        
class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, obj, markers=None):
         if isinstance(obj, Decimal):
            return str(obj)
         raise TypeError
         
class NumpyEncoder(json.JSONEncoder):

    def default(self, obj):
        """If input object is an ndarray it will be converted into a dict 
        holding dtype, shape and the data, base64 encoded.
        """
        if isinstance(obj, np.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = np.ascontiguousarray(obj)
                assert(cont_obj.flags['C_CONTIGUOUS'])
                obj_data = cont_obj.data
            data_b64 = base64.b64encode(obj_data)
            return dict(__ndarray__=data_b64,
                        dtype=str(obj.dtype),
                        shape=obj.shape)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder(self, obj)
    
    
    
class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray) and obj.ndim == 1:
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)