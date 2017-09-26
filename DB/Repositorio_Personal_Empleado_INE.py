# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryPersonalEmpleadoINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE DIAS DE ESTANCIA MEDIA EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalPersonalEmpleadoEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  