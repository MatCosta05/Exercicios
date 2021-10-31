from fastapi import FastAPI

from pydantic import BaseModel
#uvicorn ex_api:app --reload

app = FastAPI()

@app.get("/")
async def root():
    return{"Bem vindo!"}

class Resp(BaseModel):
    valor1: int
    valor2: int
    operação: str

@app.post("/exapi")
async def exapi(resp: Resp):
    return resp


