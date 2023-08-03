import numpy as np

TAM = 5
# Crear un tablero de juego 5x5
def crearTablero(tam):
    tablero = np.zeros((tam , tam))
    return tablero

# Colocar tres barcos en posiciones aleatorias
def ColocarBarcos(tablero , cant):
    while cant != 0:
      x, y = np.random.randint(0, 5, size=2)
         if tablero[x , y] == 0
            tablero[x,y] = 1
             cant -= 1
    return tablero

# Función para verificar si hay un barco o agua en las coordenadas dadas


# Prueba la función con algunas coordenadas


#Programa>> a JUGAR!
tabreal = crearTablero(TAM)
print("Tablero INICIAL\n")
print(tabreal)

ColocarBarcos(tabreal)
print("Tablero con BARCOS\n")
print(tabreal)