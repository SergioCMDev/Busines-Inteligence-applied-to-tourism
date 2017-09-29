# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryGradoOcupacionPlazasINE():
    
    
    #####################################################################################################################################################################
    ##################################GRADO DE OCUPACION POR PLAZAS EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
        
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorPlazasEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  