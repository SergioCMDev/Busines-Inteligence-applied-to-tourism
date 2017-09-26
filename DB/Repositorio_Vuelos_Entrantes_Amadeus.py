# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Amadeus import MySQLAccessAmadeus as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local


class BDRepositorioVuelosEntrantesAmadeus():
    
    
    
      


    #####################################################################################################################################################################
    #########################################VUELOS ENTRANTES#########################################
    #####################################################################################################################################################################

    def ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(self, PaisDestino,anioInicio,anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusSeparandoPorCiudadesDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusTotalesDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusTotalesEnUnAnioDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(self, PaisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoMesAnioMinMax(PaisDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, str(Anio)), self.labels ) 

    def ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusMensualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, mes, anioInicio,anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, mes, str(Anio)), self.labels ) 
    
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(self, PaisDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnio(PaisDestino, mes, str(Anio)), self.labels ) 
    
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 
    
   
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(self, PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(self, PaisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesDadoPaisDestinoAnioMinMaxSeparandoPorCiudades(PaisDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(self, PaisDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnMesEnUnAnioDadoPaisDestinoAnioSeparandoPorCiudades(PaisDestino, mes, str(Anio)), self.labels ) 

  