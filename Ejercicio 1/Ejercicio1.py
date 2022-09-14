class Paciente:
    def __init__(self,nom,ape):
        self.nombre = nom
        self.apellido = ape
    
    def __str__(self):
        return f"""Nombre: {self.nombre}
Apellido: {self.apellido} """

class ColaDePacientes:
    def __init__(self):
        self.pacientes = []

    def nuevoPaciente(self, paciente):
        self.pacientes.append(paciente)

    def pacienteActual(self):
        try:
            return self.pacientes.pop(0)
        except Exception as ex:
            print(str(ex))

    def hayCola(self):
        return self.pacientes == []
    
    def mostrarPacientes(self):
        if self.hayCola()==1: 
            print("No hay pacientes en lista de espera")
        else:
            for paciente in self.pacientes:
                print(paciente)
                print("*" *20)