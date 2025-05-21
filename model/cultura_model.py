# Classe modelo da Cultura

class CulturaModel:
    """
    CulturaModel representa uma cultura agrícola no sistema de irrigação inteligente.
    Atributos:
        id_cultura (int): Identificador único da cultura.
        nome_cultura (str): Nome da cultura.
    Métodos:
        __init__(id_cultura: int = None, nome_cultura: str = None):
            Inicializa uma nova instância de CulturaModel com os valores fornecidos.
        get_cultura_id() -> int:
            Retorna o identificador da cultura.
        set_cultura_id(id_cultura: int):
            Define o identificador da cultura.
        get_nome_cultura() -> str:
            Retorna o nome da cultura.
        set_nome_cultura(nome_cultura: str):
            Define o nome da cultura. Lança ValueError se nome_cultura for None.
    Exceções:
        ValueError: Lançada por set_nome_cultura se nome_cultura for None.
    """
    
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
    


