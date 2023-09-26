
# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
# Creamos una subclase Escritor que hereda de Autor
class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero
# Definimos una segunda clase base
class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

# Instanciamos un objeto de la clase Escritor
"""escritor = Escritor("Gabriel García Márquez", "Realismo Mágico")
print(escritor.nombre, escritor.genero)
"""
# Creamos una clase que hereda de Escritor y Academico
class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, universidad)
"""
Desafío 2: 
Implementa una clase Poeta que herede de Autor y tenga un atributo para el tipo de poesía que escribe.
"""
class Poeta(Autor):
    def __init__(self, nombre, tipo_poesia):
        super().__init__(nombre)
        self.tipo_poesia = tipo_poesia

