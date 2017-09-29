# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_Aena import MySQLAccessAena as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryVuelosSalientesAena():
    


    #####################################################################################################################################################################
    ##################################VUELOS SALIENTES####################################################
    #####################################################################################################################################################################

    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnioMinMax(self, PaisOrigen, anioInicio, anioFin): #
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Destino', 'Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAenaDadoPaisOrigenAnioMinMax(PaisOrigen, str(anioInicio), str(anioFin)), self.labels) 

   

    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(self, PaisOrigen, CityDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Anio','Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenCiudadDestinoAnio(PaisOrigen, CityDestino, str(Anio)), self.labels) 

    def ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(self, PaisOrigen):
        self.db = DBContext()
        self.labels   = ['Pais_Destino', 'Ciudad Destino','Anio', 'Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorAniosMesesDadoPaisOrigen(PaisOrigen), self.labels) 
    
    
    def ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(self, PaisOrigen, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Pais_Destino', 'CiudadDestino', 'Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosSalientesHaciaCiudadesPorDadoPaisOrigenAnioMinMaxMensualmente(PaisOrigen, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(self, PaisOrigen, Anio ):
        self.db = DBContext()
        self.labels   = ['CiudadDestino', 'Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosSalientesDivididosPorMesPorCiudadDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels) 
    
    
    def ObtenerCantidadVuelosAenaSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(self, PaisOrigen, mes, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio','Pais_Destino', 'Ciudad_Destino', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesAenaPaisesAlosQueSeViajaEnUnMesSeparadosPorAniosYCiudadesDadoPaisOrigenMesAniosMinMax(PaisOrigen, mes, str(anioInicio), str(anioFin)), self.labels) 
    
    
    def ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnio(self, PaisOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Ciudad_Destino', 'Numero_Vuelos'] 
        return (self.db.ObtenerCantidadVuelosAenaSalientesDadoPaisOrigenAnio(PaisOrigen, str(Anio)), self.labels) 

    def ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(self, PaisOrigen, CiudadDestino):
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosAenaSalientesHaciaCiudadesPorAniosMesDadoPaisOrigenCiudadDestino(PaisOrigen, CiudadDestino), self.labels) 

    def ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadOrigenAnio(self, PaisOrigen, CiudadOrigen, Anio):
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Vuelos']
        return (self.db.ObtenerCantidadVuelosAenaSalientesMensualmenteDadoPaisOrigenCiudadOrigenAnio(PaisOrigen, CiudadOrigen, str(Anio)), self.labels) 



    def ObtenerCantidadVuelosAenSalientesMensualmenteEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosSalientesMensualmenteAenaEnUnaCiudadDadoPaisOrigenCiudadDestinoAnioMinMax(PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels) 
    
    #####################################################################################################################################################################
    ########################################ENTRE VARIOS PAISES###############################
    #####################################################################################################################################################################

    def ObtenerCantidadVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, CiudadDestino, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosAenaEntreDosPaisesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisOrigen, CiudadDestino, str(anioInicio), str(anioFin)), self.labels) 
    

    def ObtenerCantidadVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(self, PaisOrigen, PaisDestino, CiudadDestino, mes, anioInicio, anioFin): 
        self.db = DBContext()
        self.labels   = ['Anio','Mes', 'Numero_Vuelos']
        return (self.db.ObtenerDatosVuelosAenaEntreDosPaisesEnUnMesDadoPaisOrigenPaisDestinoCiudadDestinoAniosMinMax(PaisOrigen, PaisDestino, CiudadDestino,mes, str(anioInicio), str(anioFin)), self.labels) 
    
