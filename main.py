from Empleado import Empleado
from Cliente import Cliente


def cargar_datos():
    respuesta = input("si va a ingresar un cliente coloque 'si' si va a ingresar un empleado coloque 'no': ")
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    cedula = input("ingrese su cedula: ")
    telefono = input("ingrese su telefono: ")

    if (respuesta == 'si'):
        categoria = input("ingrese si es 'VIP' o 'pobre'")
        cli = Cliente(nombre, apellido, cedula, telefono, categoria)
        datos_finales.append(cli)
    else:
        sueldo = input("ingrese el sueldo del trabajador: ")
        emp = Empleado(nombre, apellido, cedula, telefono, int(sueldo))
        datos_finales.append(emp)


datos_finales = []
cargar_datos()

for data in datos_finales:
    print(data)
