from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import serial
import oracledb
from datetime import datetime
import os

def __init__(self, can_write=False):
        self.can_write = can_write
        self.connections = {}  # Dicionário para armazenar as conexões
        self.cursors = {}      # Dicionário para armazenar os cursores

load_dotenv()

app = FastAPI()

class SensorData(BaseModel):
    presenca: bool
    sensor_id: int  # ID do sensor
    area_plantio_id: int  # ID da área de plantio
    tipo_sensor: str  # Tipo de sensor (umidade, pH, presença, etc.)

def connect_to_oracle():
    try:
        connection = oracledb.connect('BPILECARTE', '250903', 'localhost:1521/XEPDB1')
        print("Conexão bem-sucedida ao banco de dados!")
        return connection
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


@app.post("/sensor")
async def receber_dados(dado: SensorData):
    print(f"Recebido: {dado.presenca}, Sensor ID: {dado.sensor_id}, Tipo Sensor: {dado.tipo_sensor}")
    
    # Conexão com o banco de dados
    conn = connect_to_oracle()
    cursor = conn.cursor()

#     # Definir tipo de leitura conforme o tipo de sensor
#     tipo_leitura = dado.tipo_sensor  # Usando o tipo do sensor para o tipo de leitura (presença, umidade, pH, etc.)
#     unidade_medida = "booleano" if dado.tipo_sensor == "presença" else "unidade"  # Se for presença, a unidade é booleano
#     valor = 1 if dado.presenca else 0  # Valor para presença (1 ou 0)

#     # Inserir os dados na tabela LEITURA_SENSOR
#     data_hora = datetime.now()

#     # SQL para inserir a leitura
#     insert_query = """
#     INSERT INTO LEITURA_SENSOR (SENSOR_id_sensor, SENSOR_id_area_plantio, data_hora, valor, tipo_leitura, unidade_medida)
#     VALUES (:sensor_id, :area_plantio_id, :data_hora, :valor, :tipo_leitura, :unidade_medida)
#     """
    
#     # Executar a inserção no banco
#     cursor.execute(insert_query, {
#         'sensor_id': dado.sensor_id,
#         'area_plantio_id': dado.area_plantio_id,
#         'data_hora': data_hora,
#         'valor': valor,
#         'tipo_leitura': tipo_leitura,
#         'unidade_medida': unidade_medida
#     })

    # # Confirmar a transação
    # conn.commit()

    # # Fechar a conexão
    # cursor.close()
    # conn.close()

    # return {"mensagem": "Dado de leitura armazenado com sucesso", "presenca": dado.presenca, "tipo_leitura": tipo_leitura}
