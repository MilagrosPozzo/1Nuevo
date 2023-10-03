"""
Crea una clase Musico que tenga un método instrumento y 
crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. 
Instancia objetos de estas clases y demuestra el polimorfismo.
"""

class Musico:
    def __init__(self, instrumento):
        self.instrumento = instrumento

class Guitarrista(Musico):
    def __init__(self, instrumento):
        super().__init__(instrumento)

class Baterista(Musico):
    def __init__(self, instrumento):
       super().__init__(instrumento)

mibaterista = Baterista("Bateria")
miguitarrista = Guitarrista ("Guitarra")
print(mibaterista.instrumento, miguitarrista.instrumento)