# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryNumeroApartamentosEstimadosINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE APARTAMENTOS ESTIMADOS EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerNumeroApartamentosEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroApartamentosEstimadosEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Cantidad']
        return (self.db.ObtenerNumeroApartamentosEstimadosEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    
    def ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroApartamentosEstimadosEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  
