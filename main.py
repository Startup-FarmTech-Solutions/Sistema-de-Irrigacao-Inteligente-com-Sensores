import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from connection.connection_db import ConnectionDB
from controller.area_plantio_controller import AreaPlantioController
from controller.cultura_controller import CulturaController
from controller.sensor_controller import SensorController

# Antes de rodar o progama tem que criar um arquivo .venv na pasta `sensor_solo` porque a arquiterura é de microservisos.
# Antes de rodar o progama tem que criar um arquivo .venv na pasta `dashboard` porque a arquiterura é de microservisos.

if __name__ == "__main__":
    # connection = ConnectionDB()
    # connection.connect_to_oracle() # Conecte ao banco de dados
    # CulturaController().create_cultura()
    # CulturaController().menu_cultura()
    # CulturaController().get_culturas(connection)
    # SensorController().create_sensor()
   
    AreaPlantioController().create_area_plantio()