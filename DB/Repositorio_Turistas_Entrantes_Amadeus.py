# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: wesrok
"""
from ..DB.MySQL_Amadeus import MySQLAccessAmadeus as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local


class BDRepositorioTuristasEntrantesAmadeus():
    
    #####################################################################################################################################################################
    #########################################DESTINOS Y NUMERO TURISTAS ENTRANTES EN DESTINO#########################################
    #####################################################################################################################################################################


    def ObtenerNumeroTuristasEntrantesAnualmenteEnMesesAmadeusDadoPaisDestinoCiudadDestiniAnioMinMaxSeparado(self, PaisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasEntrantesAnualmenteEnMesesAmadeusDadoPaisDestinoCiudadDestiniAnioMinMaxSeparado(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 
    
    
    
    
    def ObtenerNumeroTuristasEntrantesAnualmenteEnMesesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasEntrantesAnualmenteEnMesesAmadeusDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), self.labels ) 
    


    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(self, PaisDestino, anioInicio, AnioFin): #OK
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Pais_Origen', 'Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses(PaisDestino, str(anioInicio), str(AnioFin)), self.labels ) 
    
    
    def ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(self, PaisDestino, CiudadDestino, Anio): #OK
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerDatosVuelosEntrantesAmadeusEnUnAnioMensualmenteDadoPaisDestinoCiudadDestinoAnio(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 
    

    def ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, AnioFin): #OK
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(AnioFin)), self.labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(self, PaisDestino, CiudadDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), self.labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, PaisDestino, CiudadDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax(PaisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels ) 


    def ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(self, PaisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusSeparadoPorCiudadesAnualmenteDadoPaisDestinoAnioMinMax(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
    def ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(self, PaisDestino, CiudadDestino, mes, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnio(PaisDestino, CiudadDestino, mes,  str(Anio)), self.labels ) 

    def ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(self,  PaisDestino, CiudadDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(PaisDestino, CiudadDestino, str(Anio)), self.labels ) 

    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(self,  PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(self,  PaisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusMensualmenteEnUnAnioDadoPaisDestinoAnio(PaisDestino, str(Anio)), self.labels ) 
    

    def ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(self, PaisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAmadeusAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades(PaisDestino, str(anioInicio), str(anioFin)), self.labels ) 
    
