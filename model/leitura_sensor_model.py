# Classe modelo do Leitura do Sensor
from datetime import date as Date

class LeituraSensorModel:
    """
    Classe LeituraSensorModel
    Representa uma leitura realizada por um sensor em uma área de plantio, armazenando informações relevantes como data/hora da leitura, valores de temperatura, umidade, leitura do sensor LDR, pH, potássio, fósforo e status de irrigação.
    Atributos:
        id_leitura_sensor (int, opcional): Identificador único da leitura do sensor.
        id_sensor (int, opcional): Identificador do sensor que realizou a leitura.
        id_area_plantio (int, opcional): Identificador da área de plantio associada à leitura.
        data_hora (str, opcional): Data e hora em que a leitura foi realizada.
        temperatura (float, opcional): Valor da temperatura registrada pelo sensor.
        umidade (float, opcional): Valor da umidade registrada pelo sensor.
        leitura_ldr (int, opcional): Valor da leitura do sensor LDR (luminosidade).
        ph (float, opcional): Valor do pH do solo registrado.
        potassio (float, opcional): Valor do potássio presente no solo.
        fosforo (float, opcional): Valor do fósforo presente no solo.
        irrigacao (chr, opcional): Status da irrigação no momento da leitura.
    Métodos:
        get_id_leitura_sensor() -> int: Retorna o identificador da leitura do sensor.
        set_id_leitura_sensor(id_leitura_sensor: int): Define o identificador da leitura do sensor.
        get_id_sensor() -> int: Retorna o identificador do sensor.
        set_id_sensor(id_sensor: int): Define o identificador do sensor.
        get_id_area_plantio() -> int: Retorna o identificador da área de plantio.
        set_id_area_plantio(id_area_plantio: int): Define o identificador da área de plantio.
        get_data_hora() -> Date: Retorna a data e hora da leitura.
        set_data_hora(data_hora: Date): Define a data e hora da leitura.
        get_temperatura() -> float: Retorna o valor da temperatura.
        set_temperatura(temperatura: float): Define o valor da temperatura.
        get_umidade() -> float: Retorna o valor da umidade.
        set_umidade(umidade: float): Define o valor da umidade.
        get_leitura_ldr() -> int: Retorna o valor da leitura do sensor LDR.
        set_leitura_ldr(leitura_ldr: int): Define o valor da leitura do sensor LDR.
        get_ph() -> float: Retorna o valor do pH.
        set_ph(ph: float): Define o valor do pH.
        get_potassio() -> float: Retorna o valor do potássio.
        set_potassio(potassio: float): Define o valor do potássio.
        get_fosforo() -> float: Retorna o valor do fósforo.
        set_fosforo(fosforo: float): Define o valor do fósforo.
        get_irrigacao() -> str: Retorna o status da irrigação.
        set_irrigacao(irrigacao: str): Define o status da irrigação.
        __str__(): Retorna uma representação em string do objeto LeituraSensorModel.
    """
    def __init__(
            self,
            id_leitura_sensor: int = None,
            id_sensor: int = None,
            id_area_plantio: int = None,
            data_hora: str = Date.today,
            temperatura: float = None,
            umidade: float = None,
            leitura_ldr: int = None,
            ph: float = None,
            potassio: float = None,  
            fosforo: float = None,  
            irrigacao: chr = None
    ):
        self.id_leitura_sensor = id_leitura_sensor
        self.id_sensor = id_sensor
        self.id_area_plantio = id_area_plantio
        self.data_hora = data_hora
        self.temperatura = temperatura
        self.umidade = umidade
        self.leitura_ldr = leitura_ldr
        self.ph = ph
        self.potassio = potassio
        self.fosforo = fosforo
        self.irrigacao = irrigacao

    # Getters e Setters
    def get_id_leitura_sensor(self) -> int:
        return self.id_leitura_sensor

    def set_id_leitura_sensor(self, id_leitura_sensor: int):
        self.id_leitura_sensor = id_leitura_sensor

    def get_id_sensor(self) -> int:
        return self.id_sensor

    def set_id_sensor(self, id_sensor: int):
        self.id_sensor = id_sensor

    def get_id_area_plantio(self) -> int:
        return self.id_area_plantio

    def set_id_area_plantio(self, id_area_plantio: int):
        self.id_area_plantio = id_area_plantio

    def get_data_hora(self) -> Date:
        return self.data_hora

    def set_data_hora(self, data_hora: Date):
        self.data_hora = data_hora

    def get_temperatura(self) -> float:
        return self.temperatura

    def set_temperatura(self, temperatura: float):
        self.temperatura = temperatura

    def get_umidade(self) -> float:
        return self.umidade

    def set_umidade(self, umidade: float):
        self.umidade = umidade

    def get_leitura_ldr(self) -> int:
        return self.leitura_ldr

    def set_leitura_ldr(self, leitura_ldr: int):
        self.leitura_ldr = leitura_ldr

    def get_ph(self) -> float:
        return self.ph

    def set_ph(self, ph: float):
        self.ph = ph

    def get_potassio(self) -> float: 
        return self.potassio

    def set_potassio(self, potassio: float):
        self.potassio = potassio

    def get_fosforo(self) -> float: 
        return self.fosforo

    def set_fosforo(self, fosforo: float):
        self.fosforo = fosforo

    def get_irrigacao(self) -> str:
        return self.irrigacao

    def set_irrigacao(self, irrigacao: str):
        self.irrigacao = irrigacao

    def __str__(self):
        return (f"LeituraSensorModel(id_leitura_sensor={self.id_leitura_sensor}, id_sensor={self.id_sensor}, "
                f"id_area_plantio={self.id_area_plantio}, data_hora={self.data_hora}, temperatura={self.temperatura}, "
                f"umidade={self.umidade}, leitura_ldr={self.leitura_ldr}, ph={self.ph}, potassio={self.potassio}, "
                f"fosforo={self.fosforo}, irrigacao={self.irrigacao})")