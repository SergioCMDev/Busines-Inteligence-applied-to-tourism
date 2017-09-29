# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_Amadeus import MySQLAccessAmadeus as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local


class BDRepositorioVuelosSalientesAmadeus():
    
    
    
       #####################################################################################################################################################################
       #########################################VUELOS SALIENTES##########################################
       #####################################################################################################################################################################


    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(self, PaisOrigen, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudades(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(self, PaisOrigen, anioInicio,anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Mes','Ciudad_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenAnioMinMaxSeparadoPorCiudadesMensualmente(PaisOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, AnioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusAnualmenteDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(AnioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen,  CiudadOrigen, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(self, PaisOrigen, CiudadOrigen, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio','Mes','Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnioMinMax(PaisOrigen, CiudadOrigen, str(anioInicio), str(anioFin)), self.labels ) 

    def ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(self, PaisOrigen, CiudadOrigen, mes, anioInicio, anioFin):  
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnMesDadoPaisOrigenCiudadOrigenMesAnioMinMax(PaisOrigen, CiudadOrigen, mes,  str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnio(self, PaisOrigen, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusMensualmenteDadoPaisOrigenCiudadOrigenAnio(PaisOrigen, CiudadOrigen, str(Anio)), self.labels )

    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioMensualmente(PaisOrigen, str(Anio)), self.labels ) 
    
    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(self,  PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnioSeparandoPorCiudades(PaisOrigen, str(Anio)), self.labels ) 

    def ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(self, PaisOrigen, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusAnualmenteEnUnMesDadoPaisOrigenMesAnioMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(self, PaisOrigen,Anio):
        self.db = DBContext()
        self.labels   = ['Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAmadeusEnUnAnioDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels ) 
    
