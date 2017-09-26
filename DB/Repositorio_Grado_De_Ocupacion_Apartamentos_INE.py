# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryGradoOcupacionApartamentosINE():
    
    
    #####################################################################################################################################################################
    ##################################PORCENTAJE DE OCUPACION DE APARTAMENTOS EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  