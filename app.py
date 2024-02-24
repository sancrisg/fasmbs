from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost","*"],  # Reemplaza "http://localhost" con el origen de tu aplicación JavaScript
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

TOKEN = "6322284639:AAFJI2SDBmlsbFJEGsFap6bJeR6w0b929iQ"

@app.get("/enviar_mensaje/")
async def enviar_mensaje(chat_id: str, mensaje: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": mensaje}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al enviar el mensaje a Telegram")
    return {"mensaje_enviado": True}
