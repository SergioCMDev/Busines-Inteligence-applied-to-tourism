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
                      "YEAR(ine_datos.fecha) AS AÑO, "+
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
                      "YEAR(ine_datos.fecha) AS AÑO, "+
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
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensuamente(self, Ciudad, Anio):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
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
                	      "ine_datos.valor AS CANTIDAD "+
                        	"FROM "+
                        	    "ine_datos "+
                        	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                        	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                        	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                        	"WHERE "+
                        	 "ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND ine_valores_variables.name LIKE '%s  "+
                              "AND YEAR(ine_datos.fecha) >= %s AND YEAR(ine_datos.fecha) <= %s "+
                        	"GROUP BY "+
                        	    "YEAR(ine_datos.fecha)"
                                        )
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin))  
        return self.cursor   
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT "+
                	    "YEAR(ine_datos.fecha) AS AÑO, "+
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
                    	    "YEAR(ine_datos.fecha) AS AÑO, "+
                    	    "ine_datos.valor AS CANTIDAD "+
                    	"FROM "+
                        	 "ine_datos "+
                    	"JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id "+
                    	"JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id "+
                    	"JOIN ine_valores_variables ON ine_defserie_variables.var_115 = ine_valores_variables.id "+
                    	"WHERE "+
                    	    "ine_defserie.name = 'Grado de ocupación por apartamentos en fin de semana' AND YEAR(ine_datos.fecha) >= %s "+
                            "AND YEAR(ine_datos.fecha) <= %s AND ine_valores_variables.name LIKE '%%s%' AND MONTH(ine_datos.fecha) = %s  "+
                    	"GROUP BY  "+
                    	    "YEAR(ine_datos.fecha)"
                                        )
        Mes = self.ObtenerNumeroMesDadoNombre(Mes)
        self.cursor.execute(self.query,(anioInicio, anioFin, Ciudad, Mes))  
        return self.cursor                   
    
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE APARTAMENTOS EN CIUDAD#################################################################################################################################
##################################################################################################################################################################################################################################################################
     #def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnio( self, Ciudad, Anio):
     #        def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
    #                def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
    #def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        
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