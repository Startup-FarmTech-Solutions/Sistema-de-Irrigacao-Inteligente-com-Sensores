# Classe modelo do Sensor

class SensorModel:
    """
    SensorModel representa um sensor utilizado no sistema de irrigação inteligente.
    Atributos:
        id_sensor (int): Identificador único do sensor. Não pode ser None.
        modelo (str): Modelo do sensor. Não pode ser None.
        nome_sensor (str): Nome do sensor. Não pode ser None.
        tipo_sensor (str): Tipo do sensor (ex: temperatura, umidade, etc). Não pode ser None.
    Métodos:
        __init__(id_sensor, modelo, nome_sensor, tipo_sensor):
            Inicializa uma nova instância de SensorModel com os valores fornecidos.
            Lança ValueError se algum dos parâmetros obrigatórios for None.
        get_id_sensor() -> int:
            Retorna o identificador do sensor.
        set_id_sensor(id_sensor: int):
            Define o identificador do sensor. Lança ValueError se id_sensor for None.
        get_modelo() -> str:
            Retorna o modelo do sensor.
        set_modelo(modelo: str):
            Define o modelo do sensor. Lança ValueError se modelo for None.
        get_nome_sensor() -> str:
            Retorna o nome do sensor.
        set_nome_sensor(nome_sensor: str):
            Define o nome do sensor. Lança ValueError se nome_sensor for None.
        get_tipo_sensor() -> str:
            Retorna o tipo do sensor.
        set_tipo_sensor(tipo_sensor: str):
            Define o tipo do sensor. Lança ValueError se tipo_sensor for None.
        __str__():
            Retorna uma representação em string do sensor, incluindo id, modelo, nome e tipo.
    """
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