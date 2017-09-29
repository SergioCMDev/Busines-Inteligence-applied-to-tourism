# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:50:46 2017

@author: Sergio Cristauro Manzano
"""
from ..DB.MySQL_Aena import MySQLAccessAena as DBContext #Server
#from self.db.MySQL import MySQLAccess as DBContext #Local

class RepositoryTuristasEntrantesAena():
    
    
    #####################################################################################################################################################################
    ##################################DESTINO Y NUMERO TURISTAS ENTRANTES HACIA PAIS DESTINO####################################################
    #####################################################################################################################################################################

    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades( self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen','Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudades( paisDestino, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses( self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes','Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorCiudadesYMeses( paisDestino, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMax( paisDestino, str(anioInicio), str(anioFin)), self.labels) 
    
    def ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(self, paisDestino, anioInicio, anioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaAnualmenteDadoPaisDestinoAnioMinMaxSeparadoPorMeses(paisDestino, str(anioInicio), str(anioFin)), self.labels) 
  
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax( self, paisDestino, CiudadDestino, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, CiudadDestino, str(anioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, anioInicio, AnioFin):
        self.db = DBContext()
        self.labels   = ['Anio', 'Pais_Origen','Ciudad_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaAnualmenteDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, mes, str(anioInicio), str(AnioFin)), self.labels) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, Anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, mes, str(Anio)), self.labels) 
    
    def ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( self, paisDestino, CiudadDestino, mes, Anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasYPaisOrigenAenaTotalesEnUnAnioDadoPaisDestinoCiudadDestinoMesAnioMinMax( paisDestino, CiudadDestino, str(Anio)), self.labels) 
    
    def ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax( self, paisDestino, CiudadDestino, Anio): 
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoCiudadDestinoAnioMinMax(paisDestino, str(Anio)), self.labels) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio( self, paisDestino, Anio): 
        self.db = DBContext()
        self.labels   = ['Pais_Origen', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioTotalesDadoPaisDestinoAnio(paisDestino, str(Anio)), self.labels) 
    
    def ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio( self, paisDestino, Anio):
        self.db = DBContext()
        self.labels   = ['Pais_Origen','Mes', 'Numero_Turistas']
        return (self.db.ObtenerPaisOrigenYNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnio( paisDestino, str(Anio)), self.labels) 
    
    def ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen(self, paisDestino, PaisOrigen, Anio): 
        self.db = DBContext()
        self.labels   = ['Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaMensualmenteEnUnAnioDadoPaisDestinoAnioYPaisOrigen( paisDestino, PaisOrigen, str(Anio)), self.labels) 
    
    def ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax(self, paisDestino, PaisOrigen, anioInicio, AnioFin): 
        self.db = DBContext()
        self.labels   = ['Anio', 'Mes', 'Numero_Turistas']
        return (self.db.ObtenerNumeroTuristasAenaMensualmenteDadoPaisDestinoAnioPaisOrigenAnioMinMax( paisDestino, PaisOrigen, str(anioInicio), str(AnioFin)), self.labels) 
    
  
