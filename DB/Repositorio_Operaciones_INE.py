# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryOperacionesINE():
    
    
    #####################################################################################################################################################################
    ##################################OPERACIONES EN CIUDAD####################################################
    #####################################################################################################################################################################



################################################################################################################################################################################
###############################################################################        APARTAMENTOS TURISTICOS                ##################################################################
################################################################################################################################################################################




    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio','Cantidad']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnioMensualmente( CiudadDestino, str(Anio)), self.labels) 

    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Cantidad']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(anioInicio), str(anioFin)), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    
    ################################################################################################################################################################################
###############################################################################        CAMPING                ##################################################################
################################################################################################################################################################################
    
    
    
    
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  

    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    
    
    ################################################################################################################################################################################
###############################################################################        HOTELES                ##################################################################
################################################################################################################################################################################



    
    
    
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio ):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio ):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin ):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
 
    ################################################################################################################################################################################
###############################################################################        RESIDENCIAS                ##################################################################
################################################################################################################################################################################



    
    
    
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
    
