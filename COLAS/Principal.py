import EjmCola as c

cola = c.Cola ()

def encolar():
    print("Escriba los datos del cliente")
    nom = input("Nombre: ")
    ape = input("Apellidos: ")
    asu = input("Asunto: ")
    clt = c.Cliente(nom,ape,asu)
    cola.encolar(clt)
    print("Cliente agregado a la cola...")

def desencolar():
    print("Desencolando elemento")
    print(cola.desencolar())
    print("Elemento desencolado")

def mostrarCola():
    if cola.estaVacia():
        print("La cola está vacía")
    else:
        for clt in cola.elementos:
            print(clt)

def menu():
    print("Bienvenidos - Sistema de Atención Al Cliente")
    print("1. Encolar")
    print("2. Desencolar")
    print("3. Mostrar cola")
    print("4. Salir")
    op=int(input("Digite la opción: "))
    return op

def main():
    op=0
    while(op!=4):
        op= menu()
        if op==1: encolar()
        elif op==2: desencolar()
        elif op==3: mostrarCola();
        elif op==4: print("Adios...")
        else: print("Opción inválida...")

main()