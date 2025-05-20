# Classe modelo da Correção
from oracledb import Date

class CorrecaoModel:
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