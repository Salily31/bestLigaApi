from pymongo import MongoClient
from datosJugadores import datosJugadores
from varaiblesEntorno import MONGO_URL
from variablesEntorno import DATABASE
from funcionesAuxiliares import calcularMediaJugador
import json


'''
    Objetivo : Crea e inicializa la coleccion Jugadores (en caso de estar creada la elimina)
'''
def crearColeccionJugadores():

    client = MongoClient(MONGO_URL)

    #creamos la base de datos o accedemos  
    ligaDB = client[DATABASE]

    #comprobamos que la coleccion jugadores no existe , en el caso de que exista la eliminamos 
    listaColecciones = ligaDB.list_collection_names()

    if "jugadores" in listaColecciones : 
        x = ligaDB["jugadores"].drop()


    #creamos o accedemos a  la coleccion de jugadores
    jugadoresCol = ligaDB["jugadores"]

    #Inicializamos la colecion
    jugadoresCol.insert_many(datosJugadores)

'''
    Objetivo : Devuelve un Json con los datos de los jugadores , calculando posicion y media
'''
def recuperarColeccionJugadores():

    client = MongoClient(url)

    #creamos la base de datos o accedemos  
    ligaDB = client[DATABASE]

    listaColecciones  = ligaDB.list_collection_names()
    if "jugadores" not in listaColecciones : 
        crearColeccionJugadores()

    #creamos o accedemos a  la coleccion de jugadores
    jugadoresCol = ligaDB["jugadores"]

    jugadoresRecuperados = jugadoresCol.find().sort("puntos",-1)
    jugadoresEnviar = []
    indice = 1
    for jugador in jugadoresRecuperados: 
        del jugador["_id"] 
        jugador["media"] = calcularMediaJugador(jugador)  
        jugador["top"] = indice 
        jugadoresEnviar.append(jugador)
        indice += 1 

    jugadoresJson = jugadoresEnviar
    
    return jugadoresJson


