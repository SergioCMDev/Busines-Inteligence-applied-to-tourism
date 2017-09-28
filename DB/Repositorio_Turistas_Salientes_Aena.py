# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Aena import MySQLAccessAena as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryTuristasSalientesAena():
    

   

    #####################################################################################################################################################################
    ##################################TURISTAS SALIENTES####################################################
    #####################################################################################################################################################################

    def ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels)
   
    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, paisDestino, CiudadDestino, anio): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasMensualmenteAenaDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(anio)), self.labels)

    def ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(self, paisDestino,Anio): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaEnUnAnioDadoPaisDestinoAnio(paisDestino, str(Anio)), self.labels)
    

    def ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, AnioFin): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaDadoPaisDestinoAnioMinMax(paisDestino, str(anioInicio), str(AnioFin)), self.labels)



    def ObtenerNumeroTuristasAenaDadoPaisOrigenCiudadOrigenMesAnio(self, paisDestino, CiudadDestino,  Mes, Anio): 
        self.db = DBContext() 
        self.labels   = ['Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaDadoPaisOrigenCiudadOrigenMesAnio(paisDestino, CiudadDestino, Mes, str(Anio)), self.labels)



    def ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasAenaDadoPaisCiudadMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels)

 
