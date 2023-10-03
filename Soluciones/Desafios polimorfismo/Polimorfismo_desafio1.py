"""
Crea una clase Musico que tenga un método instrumento y 
crea dos subclases Guitarrista y Baterista que sobrescriban el método instrumento. 
Instancia objetos de estas clases y demuestra el polimorfismo.
"""

class Musico:
    def instrumento(self):
        pass

class Guitarrista(Musico):
    def instrumento(self):
        return "toca la guitarra"

class Baterista(Musico):
    def instrumento(self):
        return "toca la bateria"

def main():
    miguitarrista = Guitarrista()
    mibaterista = Baterista()

    print(mibaterista.instrumento())
    print(miguitarrista.instrumento())

if __name__ =="__main__":
    main()