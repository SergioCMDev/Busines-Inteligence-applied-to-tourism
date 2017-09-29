# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryNumeroPlazasEstimadasINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE DIAS DE PLAZAS ESTIMADAS EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalPlazasEstimadasEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerNumeroTotalPlazasEstimadasEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalPlazasEstimadasEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  