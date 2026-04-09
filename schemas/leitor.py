from pydantic import BaseModel, EmailStr

class LeitorCreate(BaseModel):
    id: int 
    nome: str
    email: EmailStr

class LeitorOut(Basemodel):
    id: int 
    nome: str
    email: EmailStr