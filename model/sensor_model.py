# Classe modelo do Sensor

class SensorModel:
    def __init__(self,
                 id_sensor:int=None,
                 modelo:str=None,
                 nome_sensor:str=None,
                 tipo_sensor:str=None):
    
        self.set_id_sensor(id_sensor)
        self.set_modelo(modelo)
        self.set_nome_sensor(nome_sensor)
        self.tipo_sensor = tipo_sensor


    # Getters e Setters
    def get_id_sensor(self) -> int:
        return self.id_sensor
    
    def set_id_sensor(self, id_sensor:int):
        if id_sensor is not None:
            self.id_sensor = id_sensor
        else:
            raise ValueError("id_sensor não pode ser None")

    def get_modelo(self) -> str:
        return self.modelo
    
    def set_modelo(self, modelo:str):
        if modelo is not None:
            self.modelo = modelo
        else:
            raise ValueError("modelo não pode ser None")  
        
    def get_nome_sensor(self) -> str:
        return self.nome_sensor
    
    def set_nome_sensor(self, nome_sensor:str):
        if nome_sensor is not None:
            self.nome_sensor = nome_sensor
        else:
            raise ValueError("nome_sensor não pode ser None")
        
    def get_tipo_sensor(self) -> str:  
        return self.tipo_sensor
    
    def set_tipo_sensor(self, tipo_sensor:str):
        if tipo_sensor is not None:
            self.tipo_sensor = tipo_sensor
        else:
            raise ValueError("tipo_sensor não pode ser None")
        
    def __str__(self):
        return f"Sensor ID: {self.id_sensor}, Modelo: {self.modelo}, Nome Sensor: {self.nome_sensor}, Tipo: {self.tipo_sensor}"