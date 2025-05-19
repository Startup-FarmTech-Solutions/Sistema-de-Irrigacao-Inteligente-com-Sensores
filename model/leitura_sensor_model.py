# Classe modelo do Leitura do Sensor
from datetime import datetime as Datetime

class LeituraSensorModel:
    def __init__(self,
                 id_leitura_sensor:int=None,
                 id_sensor:int=None,
                 id_area_plantio:int=None,
                 data_hora:str=Datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 temperatura:float=None,
                 umidade:float=None,
                 fosforo:float=None,
                 potassio:float=None,
                 ph:float=None
                 ):
        self.set_id_leitura_senso(id_leitura_sensor)
        self.set_sensor_id(id_sensor)
        self.set_area_plantio_id(id_area_plantio)
        self.set_data_hora(data_hora)
        self.set_temperatura(temperatura)
        self.set_umidade(umidade)
        self.set_fosforo(fosforo)
        self.set_potassio(potassio)
        self.set_ph(ph)


    # Getters e Setters
    def get_id_leitura_sensor(self) -> int:
        return self.id_leitura_sensor
    
    def set_id_leitura_sensor(self, id_leitura_sensor:int):
        if id_leitura_sensor is not None:
            self.id_leitura_sensor = id_leitura_sensor
        else:
            raise ValueError("id_leitura_sensor não pode ser None")
        
    def get_id_sensor(self) -> int:
        return self.id_sensor
    
    def set_id_sensor(self, id_sensor:int):
        if id_sensor is not None:
            self.id_sensor = id_sensor
        else:
            raise ValueError("id_sensor não pode ser None")
        
    def get_id_area_plantio(self) -> int:
        return self.id_area_plantio
    
    def set_id_area_plantio(self, id_area_plantio:int):
        if id_area_plantio is not None:
            self.id_area_plantio = id_area_plantio
        else:
            raise ValueError("id_area_plantio não pode ser None")
        
    def get_data_hora(self) -> Datetime:
        return self.data_hora
    
    def set_data_hora(self, data_hora:Datetime):
        if data_hora is not None:
            self.data_hora = data_hora
        else:
            raise ValueError("data_hora não pode ser None")
        
    def get_temperatura(self) -> float:
        return self.temperatura
    
    def set_temperatura(self, temperatura:float):
        if temperatura is not None:
            self.temperatura = temperatura
        else:
            raise ValueError("temperatura não pode ser None")
        
    def get_umidade(self) -> float:
        return self.umidade
    
    def set_umidade(self, umidade:float):
        if umidade is not None:
            self.umidade = umidade
        else:
            raise ValueError("umidade não pode ser None")
        
    def get_fosforo(self) -> float:
        return self.fosforo
    
    def set_fosforo(self, fosforo:float):
        if fosforo is not None:
            self.fosforo = fosforo
        else:
            raise ValueError("fosforo não pode ser None")
        
    def get_potassio(self) -> float:
        return self.potassio
    
    def set_potassio(self, potassio:float):
        if potassio is not None:
            self.potassio = potassio
        else:
            raise ValueError("potassio não pode ser None")
        
    def get_ph(self) -> float:
        return self.ph
    
    def set_ph(self, ph:float):
        if ph is not None:
            self.ph = ph
        else:
            raise ValueError("ph não pode ser None")
        
    def __str__(self):
        return f"LeituraSensorModel(id_leitura_sensor={self.id_leitura_sensor}, id_sensor={self.id_sensor}, id_area_plantio={self.id_area_plantio}, data_hora={self.data_hora}, temperatura={self.temperatura}, umidade={self.umidade}, fosforo={self.fosforo}, potassio={self.potassio}, ph={self.ph})"
    
    

        