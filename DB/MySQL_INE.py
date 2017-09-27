# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 12:28:06 2017

@author: wesrok
"""
#import pymysql
import mysql.connector
from ..Utilidades.Constantes import Constantes
class MySQLAccessINE:
    
    connection = mysql.connector.connect(user=Constantes.UsuarioBD, host=Constantes.IP_BD, database=Constantes.DB_Name)
    def __init__(self):
#        super(MySQLAccess, self).__init__()
        print("Clase MYSQL INE Cargada Correctamente ")


    def ObtenerNumeroMesDadoNombre(self, Mes):
        if Mes == 'Enero':
            return '1'
        elif Mes == 'Febrero':
            return '2'
        elif Mes == 'Marzo':
            return '3'
        elif Mes == 'Abril':
            return '4'
        elif Mes == 'Mayo':
            return '5'
        elif Mes == 'Junio':
            return '6'
        elif Mes == 'Julio':
            return '7'
        elif Mes == 'Agosto':
            return '8'
        elif Mes == 'Septiembre':
            return '9'
        elif Mes == 'Octubre':
            return '10'
        elif Mes == 'Noviembre':
            return '11'
        elif Mes == 'Diciembre':
            return '12'
    
##################################################################################################################################################################################################################################################################
##################################################################################################################DIAS DE ESTANCIA MEDIA ESTIMADOS#################################################################################################################################
##################################################################################################################################################################################################################################################################
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (" SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                      "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                      "ine_defserie.name = 'Estancia Media' AND ine_valores_variables.name = %s AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <=  %s "+
                      "GROUP BY "+
                      "YEAR(ine_datos.fecha)")
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
      self.cursor = self.connection.cursor()
      self.query = (" SELECT "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                      "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                      "ine_defserie.name = 'Estancia Media' AND ine_valores_variables.name = %s AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                      "GROUP BY "+
                      "YEAR(ine_datos.fecha), "+
                      "MONTH(ine_datos.fecha)")
      self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
      return self.cursor
  
    
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosMensualmente( self, Ciudad, anioInicio, anioFin):
      self.cursor = self.connection.cursor()
      self.query = (" SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                      "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                      "ine_defserie.name = 'Estancia Media' AND ine_valores_variables.name = %s AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                      "GROUP BY "+
                      "YEAR(ine_datos.fecha), "+
                      "MONTH(ine_datos.fecha)")
      self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
      return self.cursor
  
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
      self.cursor = self.connection.cursor()
      self.query = (" SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                      "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                      "ine_defserie.name = 'Estancia Media' AND ine_valores_variables.name = %s AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <=  %s "+
                      "GROUP BY "+
                      "YEAR(ine_datos.fecha)")
      self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
      return self.cursor
    
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = (" 	SELECT "+
	                  "YEAR(ine_datos.fecha), "+
	                  "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
	                  "ine_datos "+
                	    "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                	    "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                	     "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                        	"WHERE "+
                	    "ine_defserie.name = 'Estancia Media' AND ine_valores_variables.name = %s AND YEAR(ine_datos.fecha) >= %s "+
                        "AND YEAR(ine_datos.fecha) <=  %s AND MONTH(ine_datos.fecha) = %s "+
                	    "GROUP BY "+
                	    "YEAR(ine_datos.fecha), "+
                	    "MONTH(ine_datos.fecha)")
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor




##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE HABITACIONES EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
    def ObtenerPorcentajeDelGradoDeOcupacionPorHabitacionesEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por habitaciones' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorHabitacionesEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha), "+
                      "ine_datos.valor AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por habitaciones' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
        
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorHabitacionesEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por habitaciones' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
        
        
        
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorHabitacionesEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha), "+
                      "ine_datos.valor AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por habitaciones' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorHabitacionesEnCiudadEnAnioEnMes(self, Ciudad, anioInicio, anioFin, Mes):
      self.cursor = self.connection.cursor()
      self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por habitaciones' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  AND MONTH(ine_datos.fecha) = %s"+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
      Mes = self.ObtenerNumeroMesDadoNombre(Mes)
      self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
      return self.cursor


##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION POR PLAZAS EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
 
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
      self.cursor = self.connection.cursor()
      self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
      self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
      return self.cursor
  
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  AND MONTH(ine_datos.fecha) = %s"+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor
    
    
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION POR PLAZAS EN FIN DE SEMANA EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
 
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnFinDeSemanaEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas en fin de semana' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnFinDeSemanaEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas en fin de semana' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnFinDeSemanaEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
      self.cursor = self.connection.cursor()
      self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas en fin de semana' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
      self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
      return self.cursor
  
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnFinDeSemanaEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas en fin de semana' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnFinDeSemanaEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por plazas en fin de semana' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  AND MONTH(ine_datos.fecha) = %s"+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################NUMERO DE APARTAMENTOS ESTIMADOS EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
 
    
    
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de apartamentos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de apartamentos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de apartamentos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de apartamentos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de apartamentos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  AND MONTH(ine_datos.fecha) = %s"+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor
    
    
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################NUMERO DE ESTABLECIMIENTOS ABIERTOS ESTIMADOS EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
 
    
    
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de establecimientos abiertos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de establecimientos abiertos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de establecimientos abiertos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de establecimientos abiertos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de establecimientos abiertos estimados' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  AND MONTH(ine_datos.fecha) = %s"+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################NUMERO DE HABITACIONES ESTIMADAS EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
 
    
    
    def ObtenerNumeroTotalHabitacionesEstimadasEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de habitaciones estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerNumeroTotalHabitacionesEstimadasEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de habitaciones estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerNumeroTotalHabitacionesEstimadasEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de habitaciones estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def  ObtenerNumeroTotalHabitacionesEstimadasEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "MONTH(ine_datos.fecha) AS MES, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de habitaciones estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroTotalHabitacionesEstimadasEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "SUM(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Número de habitaciones estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  AND MONTH(ine_datos.fecha) = %s"+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE APARTAMENTOS EN CIUDAD EN FIN DE SEMANA#################################################################################################################################
#################################################################################################################################################################################################################################################################
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensualmente(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                     "YEAR(ine_datos.fecha) AS ANIO, "+
                		"MONTH(ine_datos.fecha) AS MES, "+
                	    "ine_datos.valor AS CANTIDAD "+
                        	"FROM "+
                        	    "ine_datos "+
                        	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                        	"WHERE "+
                        	 "ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND ine_valores_variables.name = %s  "+
                              "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                        	"GROUP BY "+
                        	    "YEAR(ine_datos.fecha), "+
                        	    "MONTH(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor   
      
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                	      "AVG(ine_datos.valor) AS CANTIDAD "+
                        	"FROM "+
                        	    "ine_datos "+
                        	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                        	"WHERE "+
                        	 "ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND ine_valores_variables.name =  %s  "+
                              "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                        	"GROUP BY "+
                        	    "YEAR(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor   
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                	    "YEAR(ine_datos.fecha) AS ANIO, "+
                	    "MONTH(ine_datos.fecha) AS MES, "+
                	    "ine_datos.valor AS CANTIDAD "+
                	"FROM "+
                	    "ine_datos "+
                	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                	"WHERE "+
                	 "   ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND ine_valores_variables.name = %s  "+
                     "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                	"GROUP BY "+
                	    "YEAR(ine_datos.fecha), "+
                	    "MONTH(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor   
    
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                    	    "YEAR(ine_datos.fecha) AS ANIO, "+
                    	    "ine_datos.valor AS CANTIDAD "+
                    	"FROM "+
                        	 "ine_datos "+
                    	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                    	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                    	"WHERE "+
                    	    "ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND YEAR(ine_datos.fecha) >= %s "+
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_valores_variables.name = %s AND MONTH(ine_datos.fecha) = %s  "+
                    	"GROUP BY  "+
                    	    "YEAR(ine_datos.fecha)"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(anioInicio, anioFin, Ciudad, Mes))  
        return self.cursor                   
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE APARTAMENTOS EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                      "AVG(ine_datos.valor) AS CANTIDAD "+
                      "FROM "+
                          "ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                      "WHERE "+
                          "ine_defserie.name = 'Grado de ocupación por apartamentos' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnioMensualmente(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                     "YEAR(ine_datos.fecha) AS ANIO, "+
                		"MONTH(ine_datos.fecha) AS MES, "+
                	    "ine_datos.valor AS CANTIDAD "+
                        	"FROM "+
                        	    "ine_datos "+
                        	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                        	"WHERE "+
                        	 "ine_defserie.name = 'Grado de ocupación por apartamentos' AND ine_valores_variables.name = %s  "+
                              "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                        	"GROUP BY "+
                        	    "YEAR(ine_datos.fecha), "+
                        	    "MONTH(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor   
      
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                      "YEAR(ine_datos.fecha) AS ANIO, "+
                	      "ine_datos.valor AS CANTIDAD "+
                        	"FROM "+
                        	    "ine_datos "+
                        	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                        	"WHERE "+
                        	 "ine_defserie.name = 'Grado de ocupación por apartamentos' AND ine_valores_variables.name =  %s  "+
                              "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                        	"GROUP BY "+
                        	    "YEAR(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor   
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                	    "YEAR(ine_datos.fecha) AS ANIO, "+
                	    "MONTH(ine_datos.fecha) AS MES, "+
                	    "ine_datos.valor AS CANTIDAD "+
                	"FROM "+
                	    "ine_datos "+
                	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                	"WHERE "+
                	 "   ine_defserie.name = 'Grado de ocupación por apartamentos' AND ine_valores_variables.name = %s  "+
                     "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                	"GROUP BY "+
                	    "YEAR(ine_datos.fecha), "+
                	    "MONTH(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor   
    
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                    	    "YEAR(ine_datos.fecha) AS ANIO, "+
                    	    "ine_datos.valor AS CANTIDAD "+
                    	"FROM "+
                        	 "ine_datos "+
                    	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                    	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                    	"WHERE "+
                    	    "ine_defserie.name = 'Grado de ocupación por apartamentos' AND YEAR(ine_datos.fecha) >= %s "+
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_valores_variables.name = %s AND MONTH(ine_datos.fecha) = %s  "+
                    	"GROUP BY  "+
                    	    "YEAR(ine_datos.fecha)"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(anioInicio, anioFin, Ciudad, Mes))  
        return self.cursor              
        
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE PARCELAS EN FIN DE SEMANA EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
     #  def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio( self, Ciudad, Anio):
     # def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio( self, Ciudad, Anio):
     #     def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio(self, Ciudad, anioInicio, anioFin):
     #                          def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio(self, Ciudad, anioInicio, anioFin, Mes):
                                   
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE PARCELAS EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
   # def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnCiudadEnAnio( self, Ciudad, Anio):
  #  def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
  #  def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnCiudadEnAnio(self, Ciudad, anioInicio, anioFin):
  #  def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnCiudadEnAnio(self, Ciudad, anioInicio, anioFin, Mes):