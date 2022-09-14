import Ejercicio1 as p
import time

cola = p.ColaDePacientes()

def encolar():
    print("Escriba los datos del paciente")
    nom = input("Nombre: ")
    ape = input("Apellidos: ")
    pac = p.Paciente(nom,ape)
    cola.nuevoPaciente(pac)
    print("Agregando paciente...")
    time.sleep(2)
    print("Paciente agregado a la cola")

def desencolar():
    print("Atendiendo Paciente...")
    print(cola.pacienteActual())
    time.sleep(2)
    print("Paciente atendido")

def mostrarCola():
    cola.mostrarPacientes()

def menu():
    print("Bienvenidos - Sistema de Atención Al Cliente")
    print("1. Añadir Paciente")
    print("2. Atender Paciente")
    print("3. Mostrar cola de Pacientes")
    print("4. Salir")
    op=int(input("Digite la opción: "))
    return op

def main():
    try:
        op=0
        while(op!=4):
            op= menu()
            if op==1: encolar()
            elif op==2: desencolar()
            elif op==3: mostrarCola();
            elif op==4: print("Hasta la vista...")
            else: print("Opción inválida...")
    except Exception as ex:
        print("Error", str(ex))
        
main()