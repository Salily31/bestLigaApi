from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from herramientasDB import * 
import uvicorn

app = FastAPI(title="TheBestLiga API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/listaJugadores")
def getListaJugadores():
    listaJugadores = recuperarColeccionJugadores()
    return listaJugadores
