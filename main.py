from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AdditionRequest(BaseModel):
    x: int
    y: int

@app.get("/")
def home():
    return {"message": "Salut l'équipe ! Mon API marche bien !"}

@app.get("/dire-bonjour")
def dire_bonjour(nom: str = "inconnu"):
    return {"message": f"Bonjour {nom} !"}

@app.post("/addition")
def additionner(request: AdditionRequest):  # Utilise le modèle
    return {"resultat": request.x + request.y}