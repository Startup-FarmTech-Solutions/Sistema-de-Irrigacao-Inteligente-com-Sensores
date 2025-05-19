# Classe modelo da Área de Plantio  

class AreaPlantioModel:
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
        
