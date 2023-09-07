class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")


class Libro:
    def __init__(self, titulo , genero, ISBN, autor):
         self.titulo = titulo
         self.genero = genero
         self.ISBN = ISBN
         self.autor = autor

    def mostrar_libro(self):
        print(f"Nombre: {self.titulo}")
        print(f"Nacionalidad: {self.genero}")
        print(f"libro: {self.ISBN}")
        self.autor.mostrar_autor()
        
autor1 = Autor("Gabriel García Márquez", "Colombiano")
libro1=Libro("aa", "drama", "1234", autor1)

libro1.mostrar_libro()
