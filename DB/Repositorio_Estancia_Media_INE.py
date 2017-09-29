# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryEstanciaMediaINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE DIAS DE ESTANCIA MEDIA EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Mes','Cantidad']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosMensualmente( self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 

    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  