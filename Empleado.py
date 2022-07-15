from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, cedula, telefono, sueldo):
        super().__init__(nombre, apellido, cedula, telefono)
        self.sueldo = sueldo
