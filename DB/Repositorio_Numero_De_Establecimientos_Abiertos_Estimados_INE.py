# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryNumeroEstablecimientosAbiertosEstimadosINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE ESTABLECIMIENTOS ABIERTOS ESTIMADOS EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
        
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    
    def ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']

        return (self.db.ObtenerNumeroEstablecimientosAbiertosEstimadosEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  