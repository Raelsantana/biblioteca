from fastapi import fastapi
from api.routes.Leitores import router as leitores_router
from api.routes.livros import router as livros_router

app =  FastAPI(title="Biblioteca API")

@app.get("/")
def home():
    return {"msg": "Biblioteca API funcionamento"}

app.include_router(leitores_router)
app.include_router(livros_router)