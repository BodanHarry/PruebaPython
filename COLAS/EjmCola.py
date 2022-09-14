class Cliente:
    def __init__(self,nom,ape,asu):
        self.nombres = nom
        self.apellidos = ape
        self.asunto = asu

    def __str__(self):
        return f"""Nombre: {self.nombres}
Apellidos: {self.apellidos}
Asunto: {self.asunto}"""

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        try:
            return self.elementos.pop(0)
        except Exception as ex:
            print(str(ex))

    def estaVacia(self):
        return self.elementos == []
