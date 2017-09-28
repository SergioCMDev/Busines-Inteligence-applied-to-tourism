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
##################################################################################################################NUMERO DE PLAZAS ESTIMADAS EN CIUDAD #################################################################################################################################
#################################################################################################################################################################################################################################################################
 
    
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnAnio( self, Ciudad, Anio):
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
                          "ine_defserie.name = 'Número de plazas estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
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
                          "ine_defserie.name = 'Número de plazas estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
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
                          "ine_defserie.name = 'Número de plazas estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def  ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
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
                          "ine_defserie.name = 'Número de plazas estimadas' AND ine_valores_variables.name = %s  "+
                          "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                      "GROUP BY "+
                          "YEAR(ine_datos.fecha), "+
                          "MONTH(ine_datos.fecha)"
                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
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
                          "ine_defserie.name = 'Número de plazas estimadas' AND ine_valores_variables.name = %s  "+
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
##################################################################################################################OPERACIONES EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
 
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Apartamentos Turisticos' "+
                        ") AND ine_defserie_variables.var_103 =( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
         
         
         
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Apartamentos Turisticos' "+
                        ") AND ine_defserie_variables.var_103 IN ( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Apartamentos Turisticos' "+
                        ") AND ine_defserie_variables.var_103 =( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor     
         
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Apartamentos Turisticos' "+
                        ") AND ine_defserie_variables.var_103 =( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND MONTH(ine_datos.fecha) = %s AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin, Mes))  
        return self.cursor     
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Apartamentos Turisticos' "+
                        ") AND ine_defserie_variables.var_103 =( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor  
    
    
    
    
    
    
    
    #######################################################################CAMPING############################################################################
    
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Campings' "+
                        ") AND ine_defserie_variables.var_103  IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
         
         
         
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Campings' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Campings' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor     
         
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Campings' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_94 = '9834' AND MONTH(ine_datos.fecha) = %s AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin, Mes))  
        return self.cursor     
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Campings' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor  
    
    
    ######################################################################## HOTELES ###################################################################################
    
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Hoteles' "+
                        ") AND ine_defserie_variables.var_103 =( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
         
         
         
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Hoteles' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Hoteles' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor     
         
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Hoteles' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND MONTH(ine_datos.fecha) = %s AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin, Mes))  
        return self.cursor     
    
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Hoteles' "+
                        ") AND ine_defserie_variables.var_103 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor  
    
    
    
        ######################################################################## RESIDENCIA ###################################################################################
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Turismo Rural' "+
                        ") AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
         
         
         
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Turismo Rural' "+
                        ") AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, Anio, Anio))  
        return self.cursor     
         
                  
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Turismo Rural' "+
                        ") AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor     
         
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Turismo Rural' "+
                        ") AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND MONTH(ine_datos.fecha) = %s AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin, Mes))  
        return self.cursor     
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM"+
                        "    ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "WHERE "+
                        "    cod_operacion =( "+
                        "    SELECT "+
                        "        id "+
                        "    FROM "+
                        "        ine_operaciones "+
                        "    WHERE NAME "+
                        "        = 'Turismo Rural' "+
                        ") AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                        "    ine_valores_variables "+
                        "WHERE NAME = "+
                        "    %s "+
                        ") AND unidad = '213' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s  "+
                        "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_94 = '9834' AND ine_defserie.name = 'Viajeros' "+
                        "GROUP BY "+
                        "    AÑO, MES"
                                        )
        self.cursor.execute(self.query,(CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor  
    
    
 ##################################################################################################################################################################################################################################################################
##################################################################################################################PERNOCTACIONES EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
     
    def ObtenerPorcentajePernoctacionesEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha), "+
                  "  AVG(ine_datos.valor) "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                "    ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "JOIN ine_valores_variables ine_valores_variables96 ON "+
                 "   ine_defserie_variables.var_96 = ine_valores_variables96.id "+
                "WHERE "+
                 "ine_defserie.name = 'Pernoctaciones' AND ine_valores_variables115.name LIKE %s "+
                 "AND ine_valores_variables96.name LIKE 'Galicia' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
                 "   YEAR(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor  
    
    def ObtenerPorcentajePernoctacionesEnCiudadEnAnioMensualmente(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha) AS AÑO, "+
                  "  MONTH(ine_datos.fecha) AS MES, "+
                   " ine_datos.valor "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                 "   ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "JOIN ine_valores_variables ine_valores_variables96 ON "+
                 "   ine_defserie_variables.var_96 = ine_valores_variables96.id "+
                "WHERE "+
                 "   ine_defserie.name = 'Pernoctaciones' AND ine_valores_variables115.name LIKE %s  "+
                 " AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
             "   AÑO,  MES "
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor  
    
    def ObtenerPorcentajePernoctacionesEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha) AS AÑO, "+
                  "  MONTH(ine_datos.fecha) AS MES, "+
                   " ine_datos.valor "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                 "   ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "JOIN ine_valores_variables ine_valores_variables96 ON "+
                 "   ine_defserie_variables.var_96 = ine_valores_variables96.id "+
                "WHERE "+
                 "   ine_defserie.name = 'Pernoctaciones' AND ine_valores_variables115.name LIKE %s  "+
                 " AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
             "   AÑO,  MES "
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor  
    
    def ObtenerPorcentajePernoctacionesEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha), "+
                  "  AVG(ine_datos.valor) "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                "    ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "JOIN ine_valores_variables ine_valores_variables96 ON "+
                 "   ine_defserie_variables.var_96 = ine_valores_variables96.id "+
                "WHERE "+
                 "ine_defserie.name = 'Pernoctaciones' AND ine_valores_variables115.name LIKE %s "+
                 " AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
                 "   YEAR(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor  
      
    def ObtenerPorcentajePernoctacionesEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha), "+
                  "  AVG(ine_datos.valor) "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                "    ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "JOIN ine_valores_variables ine_valores_variables96 ON "+
                 "   ine_defserie_variables.var_96 = ine_valores_variables96.id "+
                "WHERE "+
                 "ine_defserie.name = 'Pernoctaciones' AND ine_valores_variables115.name LIKE %s "+
                 " AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s"+
                "GROUP BY "+
                 "   YEAR(ine_datos.fecha)"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor 
    
        
        
        
        
    def ObtenerCantidadTotalPernoctacionesEnAnio(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Pernoctaciones' AND ine_defserie.unidad = '242' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                "GROUP BY "+
                    "AÑO"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
  
    def ObtenerCantidadTotalPernoctacionesEnAnioMensualmente(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "MONTH(ine_datos.fecha) AS MES, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Pernoctaciones' AND ine_defserie.unidad = '242' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                "GROUP BY "+
                    "AÑO, MES"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    
    def ObtenerCantidadTotalPernoctacionesEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Pernoctaciones' AND ine_defserie.unidad = '242' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                "GROUP BY "+
                    "AÑO"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerCantidadTotalPernoctacionesEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "MONTH(ine_datos.fecha) AS MES, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Pernoctaciones' AND ine_defserie.unidad = '242' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                "GROUP BY "+
                    "AÑO, MES"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerCantidadTotalPernoctacionesEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha), "+
                  "  AVG(ine_datos.valor) "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                "    ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "JOIN ine_valores_variables ine_valores_variables96 ON "+
                 "   ine_defserie_variables.var_96 = ine_valores_variables96.id "+
                "WHERE "+
                 "ine_defserie.name = 'Pernoctaciones' AND ine_valores_variables115.name LIKE %s "+
                 "AND ine_valores_variables96.name LIKE 'Galicia' AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s"+
                "GROUP BY "+
                 "   YEAR(ine_datos.fecha)"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor 
    
    
    
  ##################################################################################################################################################################################################################################################################
##################################################################################################################PERSONAL EMPLEADO EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Personal Empleado' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
                    "AÑO"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "MONTH(ine_datos.fecha) AS MES, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Personal Empleado' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
                    "AÑO, MES"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Personal Empleado' AND ine_valores_variables115.name LIKE %s "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
                    "AÑO"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "MONTH(ine_datos.fecha) AS MES, "+
                    "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie.id = ine_defserie_variables.defserie_id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                    "ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                    "ine_defserie.name = 'Personal Empleado' AND ine_valores_variables115.name LIKE %s  "+
                    "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY "+
                    "AÑO, MES"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha), "+
                  "  SUM(ine_datos.valor) "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                "    ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                 "ine_defserie.name = 'Personal Empleado' AND ine_valores_variables115.name LIKE %s "+
                 "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s"+
                "GROUP BY "+
                 "   YEAR(ine_datos.fecha)"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor 


##################################################################################################################################################################################################################################################################
##################################################################################################################TURISTAS ENTRANTES EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnio( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                        "SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM "+
                            "ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "JOIN ine_valores_variables ine_valores_variables115 ON "+
                            "ine_valores_variables115.id = ine_defserie_variables.var_115 "+
                        "WHERE "+
                            "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '213'  "+
                            "AND ine_valores_variables115.name LIKE %s AND YEAR(ine_datos.fecha) >= %s "+
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                        "GROUP BY "+
                            "AÑO"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                        "SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM "+
                            "ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "JOIN ine_valores_variables ine_valores_variables115 ON "+
                            "ine_valores_variables115.id = ine_defserie_variables.var_115 "+
                        "WHERE "+
                            "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '213'  "+
                            "AND ine_valores_variables115.name LIKE %s AND YEAR(ine_datos.fecha) >= %s "+ 
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                        "GROUP BY "+
                            "AÑO, MES"
                                        )
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor
        
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                        "SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM "+
                            "ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "JOIN ine_valores_variables ine_valores_variables115 ON "+
                            "ine_valores_variables115.id = ine_defserie_variables.var_115 "+
                        "WHERE "+
                            "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '213'  "+
                            "AND ine_valores_variables115.name LIKE %s AND YEAR(ine_datos.fecha) >= %s "+
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                        "GROUP BY "+
                            "AÑO"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                 "   YEAR(ine_datos.fecha) AS AÑO, "+
                  "  SUM(ine_datos.valor) "+
                "FROM "+
                 "   ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "JOIN ine_valores_variables ine_valores_variables115 ON "+
                "    ine_defserie_variables.var_115 = ine_valores_variables115.id "+
                "WHERE "+
                 "ine_defserie.name = 'Personal Empleado' AND ine_valores_variables115.name LIKE %s "+
                 "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s "+
                "GROUP BY "+
                     "AÑO"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes))  
        return self.cursor 
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                        "SELECT "+
                            "YEAR(ine_datos.fecha) AS AÑO, "+
                            "MONTH(ine_datos.fecha) AS MES, "+
                            "SUM(ine_datos.valor) AS CANTIDAD "+
                        "FROM "+
                            "ine_datos "+
                        "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        "JOIN ine_valores_variables ine_valores_variables115 ON "+
                            "ine_valores_variables115.id = ine_defserie_variables.var_115 "+
                        "WHERE "+
                            "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '213'  "+
                            "AND ine_valores_variables115.name LIKE %s AND YEAR(ine_datos.fecha) >= %s "+ 
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 = '9975' "+
                        "GROUP BY "+
                            "AÑO, MES"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosEnMes(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                        "YEAR(ine_datos.fecha) AS AÑO, "+
                        "ine_datos.valor AS CANTIDAD "+
                    "FROM "+
                        "ine_datos "+
                    "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                    "WHERE "+
                        "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                         "   id "+
                        "FROM "+
                          "  ine_valores_variables "+
                        "WHERE "+
                           " ine_valores_variables.name = %s "+
                    ") AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                     "   id "+
                    "FROM "+
                      "  ine_valores_variables "+
                    "WHERE "+
                       " ine_valores_variables.name = %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s "+
                    "GROUP BY "+
                        "AÑO ")
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes))  
        return self.cursor 
    
    
    
    def ObtenerPorcentajeTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnAnio(self, CiudadDestino, CiudadOrigen, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
            "YEAR(ine_datos.fecha) AS AÑO, "+
            "AVG(ine_datos.valor) AS CANTIDAD "+
            "FROM "+
                "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
            "WHERE "+
                "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_115 IN( "+
                    "SELECT "+
                    "     id "+
                    "FROM "+
                    "ine_valores_variables "+
                    "WHERE "+
                    "ine_valores_variables.name = %s "+
                    ") AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                    "   id "+
                    "FROM "+
                    "  ine_valores_variables "+
                    "WHERE "+
                    " ine_valores_variables.name = %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY  AÑO")
        
        self.cursor.execute(self.query,(CiudadDestino, CiudadOrigen, Anio,Anio))  
        return self.cursor 

    def ObtenerPorcentajeTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAnios(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
            "YEAR(ine_datos.fecha) AS AÑO, "+
            "AVG(ine_datos.valor) AS CANTIDAD "+
            "FROM "+
                "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
            "WHERE "+
                "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_115 IN( "+
                    "SELECT "+
                    "     id "+
                    "FROM "+
                    "ine_valores_variables "+
                    "WHERE "+
                    "ine_valores_variables.name = %s "+
                    ") AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                    "   id "+
                    "FROM "+
                    "  ine_valores_variables "+
                    "WHERE "+
                    " ine_valores_variables.name = %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                "GROUP BY  AÑO")
        self.cursor.execute(self.query,(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin))  
        return self.cursor 

    def ObtenerPorcentajeTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosMensualmente(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                "YEAR(ine_datos.fecha) AS AÑO, "+
                "MONTH(ine_datos.fecha) AS MES, "+
                "SUM(ine_datos.valor) AS CANTIDAD "+
                "FROM "+
                    "ine_datos "+
                    "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_115 IN( "+
                        "SELECT "+
                        "     id "+
                        "FROM "+
                        "ine_valores_variables "+
                        "WHERE "+
                        "ine_valores_variables.name = %s "+
                        ") AND ine_defserie_variables.var_96 IN( "+
                        "SELECT "+
                        "   id "+
                        "FROM "+
                        "  ine_valores_variables "+
                        "WHERE "+
                        " ine_valores_variables.name = %s "+
                        ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                    "GROUP BY  AÑO, MES")
        self.cursor.execute(self.query,(CiudadDestino, CiudadOrigen, AnioInicio, AnioFin))  
        return self.cursor 
    
##################################################################################################################################################################################################################################################################
##################################################################################################################TURISTAS SALIENTES EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
 
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnio(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                        "YEAR(ine_datos.fecha) AS AÑO, "+
                        "AVG(ine_datos.valor) AS PORCENTAJE "+
                    "FROM "+
                        "ine_datos "+
                    "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                    "WHERE "+
                        "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                        "SELECT "+
                         "   id "+
                        "FROM "+
                          "  ine_valores_variables "+
                        "WHERE "+
                           " ine_valores_variables.name LIKE %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 != '9975' "+
                    "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_96 != '16473' "+
                    "GROUP BY "+
                        "AÑO")
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor 
    
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAnios(self, Ciudad, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                    "SELECT "+
                        "YEAR(ine_datos.fecha) AS AÑO, "+
                        "AVG(ine_datos.valor) AS PORCENTAJE "+
                    "FROM "+
                        "ine_datos "+
                    "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                    "WHERE "+
                        "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                        "SELECT "+
                         "   id "+
                        "FROM "+
                          "  ine_valores_variables "+
                        "WHERE "+
                           " ine_valores_variables.name LIKE %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 != '9975' "+
                    "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_96 != '16473'"+
                    "GROUP BY "+
                        "AÑO")
        self.cursor.execute(self.query,(Ciudad, AnioInicio, AnioFin))  
        return self.cursor 
    
    
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosEnMes(self, Ciudad, AnioInicio, AnioFin, Mes):  
      self.cursor = self.connection.cursor()
      self.query = (    
                      "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "AVG(ine_datos.valor) AS PORCENTAJE "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                    "    id "+
                    "FROM "+
                    "    ine_valores_variables "+
                    "WHERE "+
                    "    ine_valores_variables.name LIKE %s "+
                ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s  "+
                "AND ine_defserie_variables.var_96 != '9975' AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965'  "+
                "AND ine_defserie_variables.var_96 != '16473' "+
                "GROUP BY "+
                "    AÑO ")
      Mes = self.ObtenerNumeroMesDadoNombre(Mes)
      self.cursor.execute(self.query,(Ciudad, AnioInicio, AnioFin, Mes))  
      return self.cursor 
      
      
      
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnioMensualmente(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "MONTH(ine_datos.fecha) AS MES, "+
                    "ine_datos.valor AS PORCENTAJE "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                    "    id "+
                    "FROM "+
                    "    ine_valores_variables "+
                    "WHERE "+
                    "    ine_valores_variables.name LIKE %s  "+
                ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 != '9975'  "+
                "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_96 != '16473' "+
                "GROUP BY "+
                    "AÑO, MES")
        self.cursor.execute(self.query,(Ciudad, Anio, Anio))  
        return self.cursor 
    
    
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosMensualmente(self, Ciudad, AnioInicio, AnioFin):
      self.cursor = self.connection.cursor()
      self.query = (
                "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "MONTH(ine_datos.fecha) AS MES, "+
                    "ine_datos.valor AS PORCENTAJE "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                    "    id "+
                    "FROM "+
                    "    ine_valores_variables "+
                    "WHERE "+
                    "    ine_valores_variables.name LIKE %s  "+
                ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 != '9975'  "+
                "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_96 != '16473' "+
                "GROUP BY "+
                    "AÑO, MES")
      self.cursor.execute(self.query,(Ciudad, AnioInicio, AnioFin))  
      return self.cursor 
      



    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAnios(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.cursor = self.connection.cursor()
        self.query = (
                "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "AVG(ine_datos.valor) AS PORCENTAJE "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                   "     id "+
                    "FROM "+
                  "      ine_valores_variables "+
                    "WHERE "+
                 "       ine_valores_variables.name LIKE %s "+
                ") AND ine_defserie_variables.var_115 IN( "+
                "SELECT "+
                   " id "+
                "FROM "+
                  "  ine_valores_variables "+
                "WHERE "+
                 "   ine_valores_variables.name LIKE %s "+
                ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND  "+
                "ine_defserie_variables.var_96 != '9975' AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965'  "+
                "AND ine_defserie_variables.var_96 != '16473' "+
                "GROUP BY "+
                "    AÑO")   
        self.cursor.execute(self.query,(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin))  
        return self.cursor 
      

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosMensualmente(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
          self.cursor = self.connection.cursor()
          self.query = (
                      "SELECT "+
                          "YEAR(ine_datos.fecha) AS AÑO, "+
                          "MONTH(ine_datos.fecha) AS MES, "+
                          "ine_datos.valor AS PORCENTAJE "+
                      "FROM "+
                      "  ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "WHERE "+
                       " ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                         "   ine_valores_variables "+
                        "WHERE "+
                          "  ine_valores_variables.name LIKE %s "+
                    ") AND ine_defserie_variables.var_115 IN( "+
                    "SELECT "+
                     "   id "+
                    "FROM "+
                      "  ine_valores_variables "+
                    "WHERE "+
                       " ine_valores_variables.name LIKE %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 != '9975'  "+
                    "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_96 != '16473' "+
                    "GROUP BY "+
                     "   AÑO,  MES")
          self.cursor.execute(self.query,(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin))  
          return self.cursor 
      
      
      
      
      
      
      
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnio(self, CiudadOrigen, CiudadDestino, Anio):
          self.cursor = self.connection.cursor()
          self.query = (
                "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "AVG(ine_datos.valor) AS PORCENTAJE "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                   "     id "+
                    "FROM "+
                  "      ine_valores_variables "+
                    "WHERE "+
                 "       ine_valores_variables.name LIKE %s "+
                ") AND ine_defserie_variables.var_115 IN( "+
                "SELECT "+
                   " id "+
                "FROM "+
                  "  ine_valores_variables "+
                "WHERE "+
                 "   ine_valores_variables.name LIKE %s "+
                ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND  "+
                "ine_defserie_variables.var_96 != '9975' AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965'  "+
                "AND ine_defserie_variables.var_96 != '16473' "+
                "GROUP BY "+
                "    AÑO")   
          self.cursor.execute(self.query,(CiudadOrigen, CiudadDestino, Anio, Anio))  
          return self.cursor
      
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnioMensualmente(self, CiudadOrigen, CiudadDestino, Anio):
          self.cursor = self.connection.cursor()
          self.query = (
                      "SELECT "+
                          "YEAR(ine_datos.fecha) AS AÑO, "+
                          "MONTH(ine_datos.fecha) AS MES, "+
                          "ine_datos.valor AS PORCENTAJE "+
                      "FROM "+
                      "  ine_datos "+
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                      "WHERE "+
                       " ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                        "SELECT "+
                        "    id "+
                        "FROM "+
                         "   ine_valores_variables "+
                        "WHERE "+
                          "  ine_valores_variables.name LIKE %s "+
                    ") AND ine_defserie_variables.var_115 IN( "+
                    "SELECT "+
                     "   id "+
                    "FROM "+
                      "  ine_valores_variables "+
                    "WHERE "+
                       " ine_valores_variables.name LIKE %s "+
                    ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND ine_defserie_variables.var_96 != '9975'  "+
                    "AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965' AND ine_defserie_variables.var_96 != '16473' "+
                    "GROUP BY "+
                     "   AÑO,  MES")
          self.cursor.execute(self.query,(CiudadOrigen, CiudadDestino, Anio, Anio))  
          return self.cursor 
      
    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosEnMes(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
          self.cursor = self.connection.cursor()
          self.query = (
                "SELECT "+
                    "YEAR(ine_datos.fecha) AS AÑO, "+
                    "ine_datos.valor AS PORCENTAJE "+
                "FROM "+
                    "ine_datos "+
                "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                "WHERE "+
                    "ine_defserie.name = 'Viajeros' AND ine_defserie.unidad = '50' AND ine_defserie_variables.var_96 IN( "+
                    "SELECT "+
                   "     id "+
                    "FROM "+
                  "      ine_valores_variables "+
                    "WHERE "+
                 "       ine_valores_variables.name LIKE %s "+
                ") AND ine_defserie_variables.var_115 IN( "+
                "SELECT "+
                   " id "+
                "FROM "+
                  "  ine_valores_variables "+
                "WHERE "+
                 "   ine_valores_variables.name LIKE %s "+
                ") AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s AND MONTH(ine_datos.fecha) = %s  AND "+
                "ine_defserie_variables.var_96 != '9975' AND ine_defserie_variables.var_96 != '19964' AND ine_defserie_variables.var_96 != '19965'  "+
                "AND ine_defserie_variables.var_96 != '16473' "+
                "GROUP BY "+
                "    AÑO") 
          Mes = self.ObtenerNumeroMesDadoNombre(Mes)
          self.cursor.execute(self.query,(CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes))  
          return self.cursor
      