import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from connection.connection_db import ConnectionDB
from controller.area_plantio_controller import AreaPlantioController
from controller.cultura_controller import CulturaController
from controller.leitura_sensor_controller import LeituraSensorController
from controller.sensor_controller import SensorController
from sensor_solo.main import main
from dashboard.app import main

if __name__ == "__main__":
    connection = ConnectionDB()
    connection.connect_to_oracle() # Conecte ao banco de dados
    main()
    
