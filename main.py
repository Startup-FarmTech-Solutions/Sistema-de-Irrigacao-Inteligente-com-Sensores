from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    presenca: bool

@app.post("/sensor")
async def receber_dados(dado: SensorData):
    print("Recebido:", dado.presenca)
    return {"mensagem": "Dado recebido com sucesso", "presenca": dado.presenca}
