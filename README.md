# programacion_orientada_objetos
>*tenemos 3 clases PERSONA, EMPLEADO Y CLIENTE; TAMBIEN UN MAIN*

>***main***

>aqui tendremos la funcion "cargar_datos" y crearemos las varibles q ingresaran por teclado con un "input" creamos la condicion para que ingrese o cliente o empleado tambien se le agregro dos campos uno se le agrego "categoria" y a otro "sueldo" ya que estos atributos eran propio de cada uno de ellos y no se repetian.
> se crea el arreglo "datos_finales" que es donde se guardara los datos ingresados por teclado, a ese arreglo le pasamos los valores de cliente y de empleado.
> al poner cargar_datos() estamos devolviendo a la funcion esos valores almacenados ahora para poder visualizarlos de forma correta hacemos un print a datos finales o en este caso pasamos con un for los valores de datos_finales a la variable "data" para que pueda visualizarse cada elemento

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
              
              
              
              
>***clase persona***
>esta es la clase padre aqui tendemos todos los atributos que las otras dos clases tomaran estas tienen que tener propiedades iguales para esas clases, 
creamos aqui cada atributo;  con la funcion __str__ convertimos todos los valores q retornaremos a "string" esos son los valores q retornaran para poder mostrarlos se eligieron nombre, apellido y cedula son los unicos q se visualizaran SI EN EL ARREGLO SE GUARDA TODO pero aqui solo estamos presentando los 3 mencionados

          class Persona:
              def __init__(self, nombre, apellido, cedula, telefono):
                  self.nombre = nombre
                  self.apellido = apellido
                  self.cedula = cedula
                  self.telefono = telefono

              def __str__(self):
                  return self.nombre + " " + self.apellido + " " + self.cedula
                  
                  
>**clase empleado**
> aqui maandamos a llamar a la clase persona para traer sus valores eso se lo hace con "super()" y aqui creamos alguna variable o atributo propio solo de empleado como en ese caso "sueldo" si nos percatamos no tenemos que crearr todo lo q se creo en la "clase persona" solo lo reutilizamos y agregamos

                from Persona import Persona

                class Empleado(Persona):
                    def __init__(self, nombre, apellido, cedula, telefono, sueldo):
                        super().__init__(nombre, apellido, cedula, telefono)
                        self.sueldo = sueldo
>**clase cliente**
>esta tiene la misma logica que la "clase empleado" solo q aqui agregamos un atributo propio de la clase como ejemplo "categoria"
         
                 from Persona import Persona

                  class Cliente(Persona):
                      def __init__(self,nombre, apellido, cedula, telefono, categoria ):
                          super().__init__(nombre, apellido, cedula, telefono)
                          self.categoria = categoria

