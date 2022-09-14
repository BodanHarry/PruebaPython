class Libro:
    def __init__(self,tit,aut,edi):
        self.titulo = tit
        self.autor = aut
        self.edicion = edi
    
    def __str__(self):
        return f"""Título: {self.titulo}
Autor: {self.autor} 
Edición: {self.edicion}"""

class PilaDeLibros:
    def __init__(self):
        self.libros = []

    def pushLibro(self, libro):
        self.libros.append(libro)

    def popLibro(self):
        try:
            return self.libros.pop()
        except Exception as ex:
            print(str(ex))

    def hayPilaDeLibros(self):
        return self.libros == []
    
    def mostrarLibros(self):
        if self.hayPilaDeLibros()==1: 
            print("No tienes libros en tu pila")
        else:
            for libros in self.libros:
                print(libros)
                print("*" *20)
