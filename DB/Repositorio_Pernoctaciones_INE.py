# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryPernoctacionesINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE DIAS DE ESTANCIA MEDIA EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerNumeroTotalPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnio( self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerNumeroTotalPersonasEnApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajePernoctacionesEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajePernoctacionesEnCiudadEnAnioMensualmente(self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajePernoctacionesEnCiudadEnAnioMensualmente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajePernoctacionesEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajePernoctacionesEnCiudadEnRangoAnios(Ciudad, str(anioInicio), str(anioFin)), self.labels) 
      
    def ObtenerPorcentajePernoctacionesEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajePernoctacionesEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
    
    def ObtenerCantidadTotalPernoctacionesEnAnio(self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadTotalPernoctacionesEnAnio(Ciudad, str(Anio)), self.labels) 
  
    def ObtenerCantidadTotalPernoctacionesEnAnioMensualmente(self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadTotalPernoctacionesEnAnioMensualmente(Ciudad, str(Anio)), self.labels) 
  
    def ObtenerCantidadTotalPernoctacionesEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadTotalPernoctacionesEnRangoAnios(Ciudad, str(anioInicio), str(anioFin)), self.labels) 
      
    def ObtenerCantidadTotalPernoctacionesEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadTotalPernoctacionesEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
    