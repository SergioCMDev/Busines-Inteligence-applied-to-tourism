# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_INE import MySQLAccessINE as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryTuristasSalientesINE():
    
    
    #####################################################################################################################################################################
    ##################################  NUMERO DE TURISTAS SALIENTES DE CIUDAD                                        ####################################################
    ####################################################################################################################################################################

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnio(self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnio(Ciudad, str(Anio) ), self.labels) 
    


    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnioMensualmente(self, Ciudad, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnAnioMensualmente(Ciudad, str(Anio) ), self.labels)

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAnios(self, Ciudad, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAnios(Ciudad, str(AnioInicio), str(AnioFin) ), self.labels) 
    
    
    

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosMensualmente(self, Ciudad, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosMensualmente(Ciudad, str(AnioInicio), str(AnioFin) ), self.labels) 
    

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosEnMes(self, Ciudad, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadEnRangoAniosEnMes(Ciudad, str(AnioInicio), str(AnioFin), Mes ), self.labels) 
    

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosMensualmente(self, CiudadDestino, CiudadOrigen, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosMensualmente(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin) ), self.labels) 

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAnios(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAnios(CiudadOrigen , CiudadDestino, str(AnioInicio), str(AnioFin) ), self.labels) 
    

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnio(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnio(CiudadOrigen, CiudadDestino, str(Anio) ), self.labels) 

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnioMensualmente(self, CiudadOrigen, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnAnioMensualmente(CiudadOrigen, CiudadDestino, str(Anio)), self.labels) 
    

    def ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosEnMes(self, CiudadOrigen, CiudadDestino, AnioInicio, AnioFin, Mes):
        self.db = DBContext()
        self.labels   = ['Anio', 'Cantidad']
        return (self.db.ObtenerPorcentajeTotalTuristasSalientesDeCiudadOrigenACiudadDestinoEnRangoAniosEnMes(CiudadOrigen, CiudadDestino, str(AnioInicio), str(AnioFin), Mes ), self.labels) 
     
    
 