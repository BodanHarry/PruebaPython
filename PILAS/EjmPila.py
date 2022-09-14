class Pila:
    """Representa una pila con operaciones de apilar, desapilar
    y verificar si está vacía"""
    
    def __init__(self):
        self.elementos=[]

    def apilar(self, elemento):
        "Agregar un elemento a la pila"
        self.elementos.append(elemento)

    def desapilar(self):
        """Devuelve el último elemento apilado y lo elimina de la
        pila. Si la pila está vacía levanta una excepción"""
        try:
            return self.elementos.pop()
        except Exception as ex:
            print("Error", str(ex))

    def esVacia(self):
        """Devuelve true si la pila está vacía y false si la pila tiene
        elementos"""
        return self.elementos==[]
