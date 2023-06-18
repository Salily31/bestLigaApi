from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from herramientasDB import * 
import uvicorn

app = FastAPI(title="TheBestLiga API")


@app.get("/listaJugadores")
def getListaJugadores():
    listaJugadores = recuperarColeccionJugadores()
    return listaJugadores
