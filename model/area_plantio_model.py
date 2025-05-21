# Classe modelo da Área de Plantio  

class AreaPlantioModel:
    """
    Classe AreaPlantioModel
    Representa uma área de plantio com informações geográficas e descrição.
    Atributos:
        id_area_plantio (int): Identificador único da área de plantio.
        area (str): Valor total da área de plantio ocupada (ex: "1000 m²").
        latitude (float): Latitude geográfica da área de plantio.
        longitude (float): Longitude geográfica da área de plantio.
        descricao_local (str): Descrição do local da área de plantio.
    Métodos:
        __init__(id_area_plantio, area, latitude, longitude, descricao_local):
            Inicializa uma nova instância da classe AreaPlantioModel.
        get_id_area_plantio() -> int:
            Retorna o identificador da área de plantio.
        set_id_area_plantio(id_area_plantio: int):
            Define o identificador da área de plantio. Lança ValueError se for None.
        get_area() -> str:
            Retorna o valor total da área de plantio.
        set_area(area: str):
            Define o valor total da área de plantio. Lança ValueError se for None.
        get_latitude() -> float:
            Retorna a latitude da área de plantio.
        set_latitude(latitude: float):
            Define a latitude da área de plantio. Lança ValueError se for None.
        get_longitude() -> float:
            Retorna a longitude da área de plantio.
        set_longitude(longitude: float):
            Define a longitude da área de plantio. Lança ValueError se for None.
        get_descricao_local() -> str:
            Retorna a descrição do local da área de plantio.
        set_descricao_local(descricao_local: str):
            Define a descrição do local da área de plantio. Lança ValueError se for None.
    Exceções:
        ValueError: Lançada quando algum dos atributos obrigatórios recebe valor None.
    """
    
    def __init__(self,
                 id_area_plantio:int=None,
                 area:str=None, # valor total da área de plantio ocupada
                 latitude:float=None,
                 longitude:float=None,
                 descricao_local:str=None):
        
        self.set_area_plantio_id(id_area_plantio)
        self.set_tipo_area(area)
        self.set_latitude(latitude)
        self.set_longitude(longitude)

        self.set_descricao_local(descricao_local)

    # Getters e Setters
    def get_id_area_plantio(self) -> int:
        return self.id_area_plantio
    
    def set_id_area_plantio(self, id_area_plantio:int):
        if id_area_plantio is not None:
            self.id_area_plantio = id_area_plantio
        else:
            raise ValueError("id_area_plantio não pode ser None")
        
    def get_area(self) -> str:
        return self.area
    
    def set_area(self, area:str):
        if area is not None:
            self.area = area
        else:
            raise ValueError("area não pode ser None") 
        
    def get_latitude(self) -> float:
        return self.latitude
    
    def set_latitude(self, latitude:float):
        if latitude is not None:
            self.latitude = latitude
        else:
            raise ValueError("latitude não pode ser None")
        
    def get_longitude(self) -> float:
        return self.longitude
    
    def set_longitude(self, longitude:float):  
        if longitude is not None:
            self.longitude = longitude
        else:
            raise ValueError("longitude não pode ser None")
        
    def get_descricao_local(self) -> str:
        return self.descricao_local
    
    def set_descricao_local(self, descricao_local:str):
        if descricao_local is not None:
            self.descricao_local = descricao_local
        else:
            raise ValueError("descricao_local não pode ser None") 
        
