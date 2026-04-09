from fastapi import  APIRouter, HTTPExpeception
from pydantic import BaseModel
from schemas.livro import LivroCreate, LivroOut
from services.biblioteca_service import (criar_livro, listar_livros, buscar_livro, alterar_preco_livro)

router = APIRouter(prefix="/livros", tags=["livros"])



class AlterarPrecoInput(BaseModel):
    preco: float

@router.post("", response_model=livroOut)
def post_livro(data: livroCreate):
    return criar_livro(data)

@router.get("", response_model=list[livroOut])
def get_livros():
    return listar_livros(data)

@router.post("/{codigo}", response_model=livroOut)
def get_livro(codigo: str):
    livro = buscar_livro(codigo)
    if not livro:
        raise HTTPExpeception(status_code=404, detail="Livro não encontrado.")
    return livro

@router.put("/{codigo}/preco", response_model=LivroOut)
def put_preco_livro(codigo: int, data: AlterarPrecoInput):
    livro = alterar_preco_livro(codigo, data: AlterarPrecoInput):
    if not livro:
        raise HTTPExpeception(status_code=404, detail="Livro não encontrado")
    return {"codigo": livro.codigo, "titulo": livro.titulo, "preco_final": livro.preco_final()}
