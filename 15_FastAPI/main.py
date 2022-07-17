from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()
app.counter = 0


class HelloResp(BaseModel):
    msg:str

class Prodact(BaseModel):
    name:str
    description: Union[str,None] = None
    price:float
    code:str
    tax : Union[float,None] = None

@app.get('/hello/{name}', response_model=HelloResp)
def root(name : str):
    return HelloResp(msg=f"Hello {name}")


@app.get('/counter')
def counter():
    app.counter+=1
    return app.counter

@app.post('/product')
def create_product(prod : Prodact):
    return prod

