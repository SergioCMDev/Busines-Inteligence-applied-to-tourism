# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryGradoOcupacionApartamentosFinDeSemanaINE():
    
    
    #####################################################################################################################################################################
    ##################################PORCENTAJE DE OCUPACION DE APARTAMENTOS EN CIUDAD EN FIN DE SEMANA####################################################
    #####################################################################################################################################################################

    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnio( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensualmente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Mes','Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensuamente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosMensualmente(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosMensualmente( Ciudad, str(anioInicio), str(anioFin)), self.labels) 


        
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAnios(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAnios( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosEnMes(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnRangoAniosEnMes(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  
