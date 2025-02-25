from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI faz com que qualquer função que venha com um decorador dela torne-se uma API
# Parâmetro é como um endpoint

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/text")
def read_texto():
    return {"Texto": "Você é um cara de sorte"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id * 2}

# Qualquer função pode ser definida e retornada pela API
# uvicorn main:app --reload -> este comando faz com que o unicorn fique verificando alterações a fim de mudar a API ou o retorno dela

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# http://127.0.0.1:8000/docs -> já traz a documentação com o fastAPI
