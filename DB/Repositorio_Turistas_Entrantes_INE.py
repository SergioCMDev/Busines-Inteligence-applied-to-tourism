# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryTuristasEntrantesINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE TURISTAS ENTRANTES EN CIUDAD####################################################
    #####################################################################################################################################################################
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerNumeroTotalTuristasEntrantesEnCiudadEnRangoAniosMensualmente(Ciudad, str(anioInicio), str(anioFin)), self.labels) 
  
    def ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosEnMes(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerNumeroTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosEnMes(CiudadDestino, CiudadOrigen, str(AnioFin), str(AnioFin), Mes), self.labels) 
  
    def ObtenerPorcentajeTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnAnio(self, CiudadDestino, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnAnio(CiudadDestino, CiudadOrigen, str(Anio)), self.labels) 
  
    def ObtenerPorcentajeTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAnios(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAnios(CiudadDestino, CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 

    def ObtenerPorcentajeTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosMensualmente(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeTuristasEntrantesEnCiudadDestinoDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadDestino, CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 
