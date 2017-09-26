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
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnio( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensuamente( self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionPorApartamentosEnFinDeSemanaEnCiudadEnAnioMensuamente( Ciudad, str(Anio)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnRangoAniosAnio(self, Ciudad, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnRangoAniosAnio( Ciudad, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio(self, Ciudad, anioInicio, anioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerPorcentajeDelGradoDeOcupacionDeParcelasEnFinDeSemanaEnCiudadEnAnio(Ciudad, str(anioInicio), str(anioFin), Mes), self.labels) 
  