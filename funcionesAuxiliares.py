
def calcularMediaJugador(jugador):
    media = jugador["tiro"] + jugador["pase"] + jugador["verticalidad"] + jugador["ritmo"] + jugador["defensa"] + jugador["porteria"]
    media = media / 6
    return int(media)  