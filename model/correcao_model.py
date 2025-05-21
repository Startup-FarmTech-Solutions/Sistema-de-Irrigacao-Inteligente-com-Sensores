# Classe modelo da Correção
from oracledb import Date

class CorrecaoModel:
    """
    Classe CorrecaoModel
    Representa uma correção realizada em uma área de plantio, armazenando informações relevantes como tipo de correção, data/hora, quantidade aplicada e valores antes e depois da correção.
    Atributos:
        id_correcao (int): Identificador único da correção. Não pode ser None.
        id_area_plantio (int): Identificador da área de plantio associada à correção. Não pode ser None.
        tipo_correcao (str): Tipo de correção realizada (ex: fertilização, irrigação, etc). Não pode ser None.
        data_hora (Date): Data e hora em que a correção foi realizada. Não pode ser None.
        quantidade_aplicada (float): Quantidade do insumo ou ação aplicada na correção. Não pode ser None.
        valor_anterior (float): Valor do parâmetro antes da correção. Não pode ser None.
        valor_corrigido (float): Valor do parâmetro após a correção. Não pode ser None.
    Métodos:
        __init__(self, id_correcao, id_area_plantio, tipo_correcao, data_hora, quantidade_aplicada, valor_anterior, valor_corrigido):
            Inicializa uma nova instância de CorrecaoModel com os valores fornecidos.
        get_id_correcao(self) -> int:
            Retorna o identificador da correção.
        set_id_correcao(self, id_correcao: int):
            Define o identificador da correção. Lança ValueError se None.
        get_id_area_plantio(self) -> int:
            Retorna o identificador da área de plantio.
        set_id_area_plantio(self, id_area_plantio: int):
            Define o identificador da área de plantio. Lança ValueError se None.
        get_tipo_correcao(self) -> str:
            Retorna o tipo de correção.
        set_tipo_correcao(self, tipo_correcao: str):
            Define o tipo de correção. Lança ValueError se None.
        get_data_hora(self) -> Date:
            Retorna a data e hora da correção.
        set_data_hora(self, data_hora: Date):
            Define a data e hora da correção. Lança ValueError se None.
        get_quantidade_aplicada(self) -> float:
            Retorna a quantidade aplicada na correção.
        set_quantidade_aplicada(self, quantidade_aplicada: float):
            Define a quantidade aplicada. Lança ValueError se None.
        get_valor_anterior(self) -> float:
            Retorna o valor anterior à correção.
        set_valor_anterior(self, valor_anterior: float):
            Define o valor anterior à correção. Lança ValueError se None.
        get_valor_corrigido(self) -> float:
            Retorna o valor corrigido após a correção.
        set_valor_corrigido(self, valor_corrigido: float):
            Define o valor corrigido. Lança ValueError se None.
        __str__(self):
            Retorna uma representação em string da instância de CorrecaoModel.
    """
    def __init__(self,
                 id_correcao:int=None,
                 id_area_plantio:int=None,
                 tipo_correcao:str=None,
                 data_hora:str=Date.today,
                 quantidade_aplicada:float=None,
                 valor_anterior:float=None,
                 valor_corrigido:float=None,
                 ):
        
        self.set_id_correcao(id_correcao)
        self.set_id_area_plantio(id_area_plantio)
        self.set_tipo_correcao(tipo_correcao)
        self.set_data_hora(data_hora)
        self.set_quantidade_aplicada(quantidade_aplicada)
        self.set_valor_anterior(valor_anterior)
        self.set_valor_corrigido(valor_corrigido)

    # Getters e Setters
    def get_id_correcao(self) -> int:
        return self.id_correcao
    
    def set_id_correcao(self, id_correcao:int):
        if id_correcao is not None:
            self.id_correcao = id_correcao
        else:
            raise ValueError("id_correcao não pode ser None")
        
    def get_id_area_plantio(self) -> int:
        return self.id_area_plantio
    
    def set_id_area_plantio(self, id_area_plantio:int):
        if id_area_plantio is not None:
            self.id_area_plantio = id_area_plantio
        else:
            raise ValueError("id_area_plantio não pode ser None")
        
    def get_tipo_correcao(self) -> str:
        return self.tipo_correcao
    
    def set_tipo_correcao(self, tipo_correcao:str):
        if tipo_correcao is not None:
            self.tipo_correcao = tipo_correcao
        else:
            raise ValueError("tipo_correcao não pode ser None")
        
    def get_data_hora(self) -> Date:
        return self.data_hora
    
    def set_data_hora(self, data_hora:Date):
        if data_hora is not None:
            self.data_hora = data_hora
        else:
            raise ValueError("data_hora não pode ser None")
        
    def get_quantidade_aplicada(self) -> float:
        return self.quantidade_aplicada
    
    def set_quantidade_aplicada(self, quantidade_aplicada:float):
        if quantidade_aplicada is not None:
            self.quantidade_aplicada = quantidade_aplicada
        else:
            raise ValueError("quantidade_aplicada não pode ser None")
        
    def get_valor_anterior(self) -> float:
        return self.valor_anterior
    
    def set_valor_anterior(self, valor_anterior:float):
        if valor_anterior is not None:
            self.valor_anterior = valor_anterior
        else:
            raise ValueError("valor_anterior não pode ser None")
        
    def get_valor_corrigido(self) -> float:
        return self.valor_corrigido
    
    def set_valor_corrigido(self, valor_corrigido:float):
        if valor_corrigido is not None:
            self.valor_corrigido = valor_corrigido
        else:
            raise ValueError("valor_corrigido não pode ser None")
        
    def __str__(self):
        return f"CorrecaoModel(id_correcao={self.id_correcao}, id_area_plantio={self.id_area_plantio}, tipo_correcao={self.tipo_correcao}, data_hora={self.data_hora}, quantidade_aplicada={self.quantidade_aplicada}, valor_anterior={self.valor_anterior}, valor_corrigido={self.valor_corrigido})"