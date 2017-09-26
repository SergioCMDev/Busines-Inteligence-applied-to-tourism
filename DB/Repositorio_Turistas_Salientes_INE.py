# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Aena import MySQLAccessAena as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryTuristasSalientesINE():
    
    
    #####################################################################################################################################################################
    ##################################DESTINO Y NUMERO TURISTAS ENTRANTES HACIA PAIS DESTINO####################################################
    #####################################################################################################################################################################

    def ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAniosMensualmente(paisDestino, str(anioInicio), str(anioFin)), self.labels) 
  
    def ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAniosEnMes( self, Ciudad, anioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(AnioFin), Mes), self.labels) 
    

    def ObtenerNumeroTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnio( self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnio(CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnioMensualmente( self, CiudadOrigen,CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnAnioMensualmente(CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 
    
    def ObtenerNumeroTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAnios(self, CiudadOrigen, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAnios(CiudadOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosMensualmente(self, CiudadOrigen, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels) 
  
    def ObtenerNumeroTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosEnMes( self, CiudadOrigen, CiudadDestino, anioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTotalTuristasSalientesDeCiudadEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, str(anioInicio), str(AnioFin), Mes), self.labels) 
    
    
