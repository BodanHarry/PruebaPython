import Ejercicio2 as l
import time

pila = l.PilaDeLibros()

def agregarLibro():
    print("Escriba los datos del libro")
    tit = input("Título: ")
    aut = input("Autor: ")
    edi = input("Edición: ")
    lib = l.Libro(tit,aut,edi)
    pila.pushLibro(lib)
    print("Agregando Libro...")
    time.sleep(2)
    print("Libro agregado a tu pila")

def quitarLibro():
    print("Quitando Libro...")
    print(pila.popLibro())
    time.sleep(2)
    print("Hemos quitado el libro")

def mostrarPila():
    pila.mostrarLibros()

def menu():
    print("Bienvenido a tu pila de libros")
    print("1. Añadir Libro")
    print("2. Quitar Libro")
    print("3. Mostrar pila de Libros")
    print("4. Salir")
    op=int(input("Digite la opción: "))
    return op

def main():
    try:
        op=0
        while(op!=4):
            op= menu()
            if op==1: agregarLibro()
            elif op==2: quitarLibro()
            elif op==3: mostrarPila();
            elif op==4: print("Hasta la vista...")
            else: print("Opción inválida...")
    except Exception as ex:
        print("Error", str(ex))
        
main()







import Ejercicio2 as l
import time

pila = l.PilaDeLibros

def menu():
    print("Bienvenido a su pila de libros")
    print("1. Ingresar Libro")
    print("2. Sacar Libros")
    print("3. Mostrar Libros")
    print("4. Salir")
    op = int(input("Digite la opción: "))
    return op

def ingresarLibro():
    print("Escriba los datos del libro")
    tit = input("Título: ")
    aut = input("Autor: ")
    edi = input("Edición: ")
    lib = l.Libro(tit,aut,edi)
    pila.pushLibro(lib)
    print("Apilando libro...")
    time.sleep(2)
    print("Libro apilado")

def sacarLibro():
    print("Sacando el libro de tu pila")
    print(pila.popLibro())
    time.sleep(2)
    print("Sacaste el libro de tu pila")

def mostrarLibros():
    pila.mostrarLibros()

def main():
    try:
        op=0
        while(op!=4):
            op= menu()
            if op==1: ingresarLibro()
            elif op==2: sacarLibro()
            elif op==3: mostrarLibros();
            elif op==4: print("Hasta la vista...")
            else: print("Opción inválida...")
    except Exception as ex:
        print("Error", str(ex))

main()