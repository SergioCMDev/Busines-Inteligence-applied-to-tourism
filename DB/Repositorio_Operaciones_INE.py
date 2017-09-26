# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryEstanciaMediaINE():
    
    
    #####################################################################################################################################################################
    ##################################NUMERO DE DIAS DE ESTANCIA MEDIA EN CIUDAD####################################################
    #####################################################################################################################################################################

    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnAnioMensualmente( self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnAnioMensualmente( CiudadOrigen, str(Anio)), self.labels) 
    
    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAnios( self, CiudadOrigen, AnioInicio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAnios( CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  

    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente( CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 

    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadOrigen, CiudadDestino, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadOrigen, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerCantidadDiasEstanciaMediaEstimadosEnCiudadEnRangoAnios( CiudadDestino, str(Anio)), self.labels) 

    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(anioInicio), str(anioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(anioInicio), str(anioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(anioInicio), str(anioFin)), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnAnioMensualmente(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAniosEnMes(self, CiudadOrigen, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAniosMensualmente(self, CiudadOrigen, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(CiudadDestino, CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(CiudadDestino, CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  

    def ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnAnioMensualmente(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnAnioMensualmente(CiudadOrigen, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAnios(self, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAniosEnMes(self, CiudadOrigen, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAniosEnMes(CiudadOrigen, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAniosMensualmente(self, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnAnio(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 
  
    
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAnios(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAnios(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAniosEnMes(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAniosMensualmente(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelDesdeCiudadOrigenHastaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio ):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio ):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin ):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnAnioMensualmente(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnAnioMensualmente(CiudadOrigen, str(Anio)), self.labels) 
  

    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAnios(self, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAniosEnMes(self, CiudadOrigen, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAnios(CiudadOrigen, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAniosMensualmente(self, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnRangoAniosMensualmente(CiudadOrigen, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 
    
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAnios(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 

    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnio(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnio(CiudadDestino, str(Anio)), self.labels) 
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnioMensualmente(self, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnAnioMensualmente(CiudadDestino, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAnios(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAnios(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosEnMes(self, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosEnMes(CiudadDestino, str(AnioInicio), str(AnioFin), Mes), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasHaciaCiudadDestinoEnRangoAniosMensualmente(CiudadDestino, str(AnioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnAnio(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasApartamentosTuristicosDesdeCiudadOrigenEnAnio(CiudadOrigen, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnAnio(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasCampingDesdeCiudadOrigenEnAnio(CiudadOrigen, str(Anio)), self.labels) 
    
    def ObtenerCantidadPersonasHotelesDesdeCiudadOrigenEnAnio(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasHotelesDesdeCiudadOrigenEnAnio(CiudadOrigen, str(Anio)), self.labels) 
  
    def ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnAnio(self, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerCantidadPersonasResidenciasDesdeCiudadOrigenEnAnio(CiudadOrigen, str(Anio)), self.labels) 
  