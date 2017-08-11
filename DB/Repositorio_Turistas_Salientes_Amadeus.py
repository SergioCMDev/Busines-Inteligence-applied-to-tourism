# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Amadeus import MySQLAccessAmadeus as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local


class BDRepositorioTuristasSalientesAmadeus():
    
    
        
       #####################################################################################################################################################################
       #########################################TURISTAS SALIENTES##########################################
       #####################################################################################################################################################################

    
    def ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen,  CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen, Anio): 
        self.db = DBContext()
        self.labels   = ['Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusSeparadoPorCiudadesMensualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels )

    def ObtenerDatosTuristasSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen, mes, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, str(Anio)), self.labels ) 
    
    def ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen,str(Anio)), self.labels ) 

    def ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen,  CiudadDestino, mes,  anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerDatosTuristasSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen,CiudadDestino, mes,  str(anioInicio), str(anioFin)), self.labels ) 


