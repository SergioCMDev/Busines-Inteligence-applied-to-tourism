# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_Aena import MySQLAccessAena as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryVuelosEntrantesAena():
    
    #####################################################################################################################################################################
    #######################################################VUELOS ENTRANTES####################################################
    #####################################################################################################################################################################
   
    def ObtenerPaisOrigenYVuelosEntrantesAenaDadoPaisDestinoAnio(self, paisDestino, anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisOrigenYVuelosEntrantesAenaDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels)

    def ObtenerPaisOrigenYVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnio(self, paisDestino, CiudadDestino, anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisOrigenYVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnio( paisDestino, CiudadDestino, str(anio)), self.labels)

    def ObtenerPaisesOrigenYVuelosEntrantesMensualmenteDuranteAniosAenaDadoPaisDestinoAnio(self, paisDestino, anio): 
        self.db = DBContext()
        self.labels   = ['Mes', 'Pais_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisesOrigenYVuelosEntrantesMensualmenteDuranteAniosAenaDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels)


    def ObtenerPaisesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels)


    def ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesDuranteAnioAenaDadoPaisDestinoAnio(self, paisDestino, anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Ciudad_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesDuranteAnioAenaDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels)


    def ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Ciudad_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels)


    def ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoMesAnioMinMax(self, paisDestino, Mes, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen', 'Numero_Vuelos']
        return (self.db.ObtenerPaisesOrigenCiudadesOrigenYVuelosEntrantesAnualmenteAenaDadoPaisDestinoMesAnioMinMax( paisDestino, Mes, str(anioInicio), str(anioFin)), self.labels)


    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels) 

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels) 

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax(self, paisDestino, mes, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoMesAnioMinMax( paisDestino, mes, str(anioInicio), str(anioFin)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio(self, paisDestino, anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDivididosPorCiudadesDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels)


    def ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(self, paisDestino, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesEnUnMesAenaDivididosPorCiudadesDadoPaisDestinoMesAnioMinMax(paisDestino, mes, str(anioInicio), str(anioFin)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio(self, paisDestino, anio): ####
        self.db = DBContext()
        self.labels   = ['Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnAnioDivididosPorCiudadDadoPaisDestinoAnio( paisDestino, str(anio)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio(self, paisDestino, mes, Anio): ##
        self.db = DBContext()
        self.labels   = ['Ciudad', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaMensualmenteDivididosPorCiudadDadoPaisDestinoMesAnio( paisDestino, mes, str(Anio)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax(self, paisDestino, CiudadDestino, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio','Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaDadoPaisDestinoCiudadDestinoAnioMinMax( paisDestino,CiudadDestino, str(anioInicio), str(anioFin)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(self, paisDestino, CiudadDestino, mes, anioInicio, anioFin): ###
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnMesDadoPaisDestinoCiudadDestinoMesAnioMinMax(paisDestino, CiudadDestino, mes, str(anioInicio), str(anioFin)), self.labels)

    def ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(self, paisDestino, CiudadDestino, Anio): ###
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosEntrantesAenaEnUnAnioEnUnaCiudadMensualmenteDadoPaisDestinoCiudadAnio(paisDestino, CiudadDestino, str(Anio)), self.labels)
  
