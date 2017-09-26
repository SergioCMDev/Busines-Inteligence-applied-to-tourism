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


    
    def ObtenerSentenciaGenericaCiudadRangoAniosSQL(Ciudad, AnioInicio, AnioFin, TipoSerie, Unidades):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT ine_datos.fecha AS FECHA"
                      "ine_datos.valor AS CANTIDAD"
                      "FROM  ine_datos"
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id"
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id"
                      "JOIN ine_operaciones ON ine_defserie.cod_operacion = ine_operaciones.id"
                      "JOIN ine_periodicidades ON ine_periodicidades.id = ine_defserie.periodicidad"
                      "JOIN ine_unidades ON ine_defserie.unidad = ine_unidades.id"
                      "JOIN ine_valores_variables ine_valores_variables94 ON  ine_defserie_variables.var_94 = ine_valores_variables94.id"
                      "JOIN ine_valores_variables ine_valores_variables115 ON  ine_defserie_variables.var_115 = ine_valores_variables115.id"
                      "JOIN ine_valores_variables ine_valores_variables96 ON ine_defserie_variables.var_96 = ine_valores_variables96.id"
                      "WHERE"
                      "   ("
                      "    LENGTH(%s)= 0 OR YEAR(ine_datos.fecha) >= %s-- AÑO INICIO"
                      " ) AND("
                      "    LENGTH(%s) = 0 OR YEAR(ine_datos.fecha) <= %s -- AÑO FIN"
                      ") AND("
                      "   LENGTH(%s) = 0 OR MONTH(ine_datos.fecha) >= %s -- MES INICIO"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_valores_variables115.name LIKE %Alicante% -- SITIO DESTINO"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_unidades.name LIKE '%%s%' -- Personas"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_operaciones.name = '%%s%' -- Tipo Operacion"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_periodicidades.name LIKE '%%s%' -- PERIODICIDAD (Mensual, Anual...)"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_valores_variables94.name LIKE '%%s%' -- TIPO SUMA CATEGORIA SERIE"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_valores_variables96.name LIKE '%%s%' -- CATEGORIA/Residencia"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_defserie.name LIKE '%%s%' -- TIPO SERIE"
                      ")")
        self.cursor.execute(self.query,(AnioInicio, AnioFin, Unidades))  
        return self.cursor
    
    def ObtenerSentenciaGenericaCiudadRangoAniosMesSQL(Ciudad, AnioInicio, AnioFin, Mes, TipoSerie, Unidades):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT  ine_datos.fecha AS FECHA"
                      "ine_datos.valor AS CANTIDAD"
                      "FROM  ine_datos"
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id"
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id"
                      "JOIN ine_operaciones ON ine_defserie.cod_operacion = ine_operaciones.id"
                      "JOIN ine_periodicidades ON ine_periodicidades.id = ine_defserie.periodicidad"
                      "JOIN ine_unidades ON ine_defserie.unidad = ine_unidades.id"
                      "JOIN ine_valores_variables ine_valores_variables94 ON  ine_defserie_variables.var_94 = ine_valores_variables94.id"
                      "JOIN ine_valores_variables ine_valores_variables115 ON  ine_defserie_variables.var_115 = ine_valores_variables115.id"
                      "JOIN ine_valores_variables ine_valores_variables96 ON ine_defserie_variables.var_96 = ine_valores_variables96.id"
                      "WHERE"
                      "   ("
                      "    LENGTH(%s)= 0 OR YEAR(ine_datos.fecha) >= %s-- AÑO INICIO"
                      " ) AND("
                      "    LENGTH(%s) = 0 OR YEAR(ine_datos.fecha) <= %s -- AÑO FIN"
                      ") AND("
                      "   LENGTH(%s) = 0 OR MONTH(ine_datos.fecha) >= %s -- MES INICIO"
                      ")AND("
                      "    LENGTH(%s) = 0 OR MONTH(ine_datos.fecha) <= %s -- MES FIN"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_valores_variables115.name LIKE %Alicante% -- SITIO DESTINO"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_unidades.name LIKE '%%s%' -- Personas"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_operaciones.name = '%%s%' -- Tipo Operacion"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_periodicidades.name LIKE '%%s%' -- PERIODICIDAD (Mensual, Anual...)"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_valores_variables94.name LIKE '%%s%' -- TIPO SUMA CATEGORIA SERIE"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_valores_variables96.name LIKE '%%s%' -- CATEGORIA/Residencia"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_defserie.name LIKE '%%s%' -- TIPO SERIE"
                      ")")
        self.cursor.execute(self.query,(anioInicio, anioFin, anioFin, Mes, TipoSerie, Unidades))  
        return self.cursor
    

    def ObtenerSentenciaGenericaCiudadRangoAniosMesSQL(CiudadOrigen, CiudadDestino, anioInicio, Mes, anioFin, TipoSerie, Unidades):
        self.cursor = self.connection.cursor()
        self.query = ("SELECT  ine_datos.fecha AS FECHA"
                      "ine_datos.valor AS CANTIDAD"
                      "FROM  ine_datos"
                      "JOIN ine_defserie_variables ON ine_datos.serie_id = ine_defserie_variables.id"
                      "JOIN ine_defserie ON ine_defserie_variables.defserie_id = ine_defserie.id"
                      "JOIN ine_operaciones ON ine_defserie.cod_operacion = ine_operaciones.id"
                      "JOIN ine_periodicidades ON ine_periodicidades.id = ine_defserie.periodicidad"
                      "JOIN ine_unidades ON ine_defserie.unidad = ine_unidades.id"
                      "JOIN ine_valores_variables ine_valores_variables94 ON  ine_defserie_variables.var_94 = ine_valores_variables94.id"
                      "JOIN ine_valores_variables ine_valores_variables115 ON  ine_defserie_variables.var_115 = ine_valores_variables115.id"
                      "JOIN ine_valores_variables ine_valores_variables96 ON ine_defserie_variables.var_96 = ine_valores_variables96.id"
                      "WHERE"
                      "   ("
                      "    LENGTH(%s)= 0 OR YEAR(ine_datos.fecha) >= %s-- AÑO INICIO"
                      " ) AND("
                      "    LENGTH(%s) = 0 OR YEAR(ine_datos.fecha) <= %s -- AÑO FIN"
                      ") AND("
                      "   LENGTH(%s) = 0 OR MONTH(ine_datos.fecha) >= %s -- MES INICIO"
                      ")AND("
                      "    LENGTH(%s) = 0 OR MONTH(ine_datos.fecha) <= %s -- MES FIN"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_valores_variables115.name LIKE %Alicante% -- SITIO DESTINO"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_unidades.name LIKE '%%s%' -- Personas"
                      ") AND("
                      "   LENGTH(%s) = 0 OR ine_operaciones.name = '%%s%' -- Tipo Operacion"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_periodicidades.name LIKE '%%s%' -- PERIODICIDAD (Mensual, Anual...)"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_valores_variables94.name LIKE '%%s%' -- TIPO SUMA CATEGORIA SERIE"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_valores_variables96.name LIKE '%%s%' -- CATEGORIA/Residencia"
                      ") AND("
                      "    LENGTH(%s) = 0 OR ine_defserie.name LIKE '%%s%' -- TIPO SERIE"
                      ")")
        self.cursor.execute(self.query,(Ciudad, anioInicio, anioFin, Mes, TipoSerie, Unidades))  
        return self.cursor
    
    
##################################################################################################################################################################################################################################################################
##################################################################################################################DIAS DE ESTANCIA MEDIA ESTIMADOS#################################################################################################################################
##################################################################################################################################################################################################################################################################
   # def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
     #   return ObtenerSentenciaGenericaSQL(Ciudad, Anio)
   #==     
    #def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
    #def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
    #def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        
        
##################################################################################################################################################################################################################################################################
##################################################################################################################PORCENTAJE DE OCUPACION DE APARTAMENTOS EN CIUDAD EN FIN DE SEMANA#################################################################################################################################
##################################################################################################################################################################################################################################################################
     # def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnio( self, Ciudad, Anio):
    #          def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensuamente( self, Ciudad, Anio):
     #                 def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnRangoAniosAnio(self, Ciudad, anioInicio, anioFin):
      #                        def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio(self, Ciudad, anioInicio, anioFin, Mes):
                                  
                                  
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