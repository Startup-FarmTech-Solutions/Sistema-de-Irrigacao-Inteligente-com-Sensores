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
<<<<<<< HEAD
from sensor_solo.main import main
=======
from dashboard.app import main
>>>>>>> 116db0e0682d447f5f09e01be09bdf5f915db754

if __name__ == "__main__":
    connection = ConnectionDB()
    connection.connect_to_oracle() # Conecte ao banco de dados
<<<<<<< HEAD
    main()
    
=======
    # CulturaController().create_cultura()
    # CulturaController().menu_cultura()
    # CulturaController().get_culturas(connection)
    # SensorController().create_sensor()
    main()
    AreaPlantioController().create_area_plantio()
>>>>>>> 116db0e0682d447f5f09e01be09bdf5f915db754
