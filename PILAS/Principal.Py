import EjmPila as p
pila = p.Pila()

def menu():
    try:
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Mostrar Pila")
        print("4. Salir")
        print("Escriba la opración a realizar: ", end="")
        op = int(input())
        return op
    except Exception as ex:
        print("Error desconocido", str(ex))

def apilarElemento():
    try:
        num = int(input("Escribe un # ebtero: "))
        pila.apilar(num)
        print("Elemento apilado...")
    except Exception as ex:
        print("Error desconocido", str(ex))

def mostrarPila():
    if(pila.esVacia()):
        print("La pila está vacía")
    else:
        cont = len(pila.elementos)-1
        print("=" * 10)
        while(cont>=0):
            num = pila.elementos[cont]
            print(num)
            print("=" * 10)
            cont-=1

def desapilarElemento():
    if(pila.esVacia()):
        print("La pila está vacía")
    else:
        print("Eliminando elemento...")
        pila.elementos.pop()
        print("Elemento eliminado")

def main():
    op=0
    while op != 4:
        op=menu()
        if op==1: apilarElemento()
        elif op==2: desapilarElemento()
        elif op==3: mostrarPila()
        elif op==4: print("Hasta la próxima...")
        else: print("Opción Invalida")

main()