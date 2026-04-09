from pydantic import BaseModel

class LivroCreate(BaseModel):
    codigo: int 
    titulo: str
    preco: float
    tipo: str
    desconto_percentual: float

class LivroOut(Basemodel):
     codigo: int 
     titulo: str
     preco: float
     tipo: str
     desconto_percentual: float
     