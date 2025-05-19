# Classe modelo da Cultura

class CulturaModel:
    def __init__(self,
                 id_cultura:int=None,
                 nome_cultura:str=None
                 ):
        
        self.set_cultura_id(id_cultura)
        self.set_nome_cultura(nome_cultura)

    # Getters e Setters
    def get_cultura_id(self) -> int:
        return self.id_cultura
    
    def set_cultura_id(self, id_cultura:int):
        self.id_cultura = id_cultura

    def get_nome_cultura(self) -> str:
        return self.nome_cultura

    def set_nome_cultura(self, nome_cultura:str):
        if nome_cultura is not None:
            self.nome_cultura = nome_cultura
        else:
            raise ValueError("nome_cultura não pode ser None")
    


