"""
Crea una clase Musico que tenga un método instrumento y 
crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. 
Instancia objetos de estas clases y demuestra el polimorfismo.
"""

class Musico:
    def __init__(self, instrumento):
        self.instrumento = instrumento

class Guitarrista(Musico):
    def __init__(self, instrumento, cuerdas):
        super().__init__(instrumento)
        self.cuerdas = cuerdas


class Baterista(Musico):
    def __init__(self, instrumento, genero):
        super().__init__(instrumento)
        self.baquetas = baquetas