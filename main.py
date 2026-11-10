
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
def main():
    return 'Hello World'

@app.get('/dobro')
def dobro(n: float):
    return n * 2

@app.get('/soma')
def soma(a: int, b: int, c:int):
    return (a + b) * c

from pydantic import BaseModel


class Teste(BaseModel):
    name: str
    age: int
    money: float 


@app.post('/saudacao')
def saudacao(pessoa: Teste):

    status = None


    if pessoa.money < 100:
        status = 'Pobre'
    elif pessoa.money < 1000:
        status = 'Miseravel'
    else: 
        status = 'Bem de Vida'

    if status == 'Pobre':
        raise HTTPException(status_code = 401, detail = 'Você não tem dinheiro suficiente para continuar!')

    return {f'Seja bem vindo: {pessoa.name}, você tem {pessoa.age} anos, e seu dinheiro é de {pessoa.money}, e seu status é {status}'}


messages = [

]

@app.get('/chat')
def chat(input: str):
    messages.append(input)

    return {
        'messages': messages
    }


import asyncio

@app.get('/async')
async def assync():
    await asyncio.sleep(4)
    return 'demorou 4s para isso retornar'

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse


@app.get("/predict", response_class=HTMLResponse)
async def predict_page():

    return """
    <html>
        <body>
            <h1>Image Classification</h1>

            <form action="/predict" method="POST"
                  enctype="multipart/form-data">

                <input type="file" name="file" accept="image/*" required>

                <button type="submit">
                    Classificar imagem
                </button>

            </form>
        </body>
    </html>
    """


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    # Aqui você executará seu modelo de ML/DL.

    prediction = "Dog"

    return {
        "filename": file.filename,
        "prediction": prediction
    }