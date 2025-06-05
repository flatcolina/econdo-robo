from fastapi import FastAPI
from pydantic import BaseModel
from robo import executar_robo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API no ar"}

class Hospede(BaseModel):
    nome: str
    data_checkin: str
    data_checkout: str
    valor: str
    comissao: str

@app.post("/executar-login")
def executar(hospede: Hospede):
    try:
        link = executar_robo(hospede.nome, hospede.data_checkin, hospede.data_checkout, hospede.valor, hospede.comissao)
        return {"status": "ok", "link": link}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}