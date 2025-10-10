calificacion = 0

print("pregunta 1: ¿cual de los siguientes componentes no es parte fundamental de la arquitectura de von neumann?")
print("1) tarjeta grafica")
print("2) memoria principal")
print("3) sistema de entrada/salida")
print("4) cpu")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 1
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 0
    case _:
        print("opcion no valida.")
        
        
print("el lenguaje maquina esta compuesto por: ")
print("1) simbolos logicos y matematicos")
print("2) pseudocodigo")
print("3) instrucciones en ingles abreviado")
print("4) codigo binario")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 1
    case _:
        print("opcion no valida.")


print("el lenguaje de programacion de alto nivel se caracteriza por: ")
print("1) ser el mas rapido en tiempo de ejecucion")
print("2) tener un control directo y preciso sobre el hardware")
print("3) ser independiente de la arquitectura de la computadora")
print("4) ser muy dificil de aprender y leer")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 1
    case 4:
        calificacion = calificacion + 0
    case _:
        print("opcion no valida.")
        

print("que es un algoritmo? ")
print("1) una secuencia de pasos finitos y bien definidos para resolver un problema ")
print("2) un lenguaje de programacion especifico")
print("3) el codigo fuente de una computadora")
print("4) un conjunto de instrucciones escritas en codigo binario")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 1
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 0
    case _:
        print("opcion no valida.")
        

print("en pseudocodico ¿que estructuras de control se utiliza para ejecutar un bloque de codigo solo si se cumple una condicion especifica?")
print("1) repetitiva mientras")
print("2) repetitiva para")
print("3) secuencial")
print("4) condicional o de seleccion")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 1
    case _:
        print("opcion no valida.")
        

print("el proposito principal de un pseudocodigo es:")
print("1) traducir automaticamente el codigo de alto nivel a lenguaje maquina")
print("2) planificar y describir la logica de un algoritmo de forma legible para los humanos ")
print("3) ejecutar programas de forma mas eficiente que un lenguaje compilado")
print("4) proporcionar un control directo sobre los registros del procesador")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 1
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 0
    case _:
        print("opcion no valida.")
        

print("un programa de computadora es esencialmente")
print("1) una coleccion de algoritmos ")
print("2) el sistema operativo de una computadora")
print("3) un dispositivo de hardware")
print("4) una secuencia de instrucciones que la computadora ejecuta")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 1
    case _:
        print("opcion no valida.")
        

print("cual es la principal diferencia entre un bucle mientras y un repetir ")
print("1) no hay ninguna diferencia son intercambiables")
print("2) el bucle repetir solo usa numeros mientras que el mientras puede usar cualquier condicion")
print("3) el buble mientras es mas rapido que el repetir")
print("4) el mientras puede no ejecutarse mientras que el repetir se ejecuta al menos una vez")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 1
    case _:
        print("opcion no valida.")
        

print("el lenguaje ensamblador es considerado un lenguaje de nivel..")
print("1) medio")
print("2) alto")
print("3) bajo")
print("4) muy alto")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 0
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 1
    case 4:
        calificacion = calificacion + 0
    case _:
        print("opcion no valida.")
        

print("que estructura de control es mas adecuada para iterar sobre una secuencia de elementos un numero conocido de veces conocido de antemano?")
print("1) bucle para")
print("2) sentencia condicional si")
print("3) bucle repetir")
print("4) bucle mientras")

respuesta = int(input("elige tu respuesta (1-4): "))

match respuesta:
    case 1:
        calificacion = calificacion + 1
    case 2:
        calificacion = calificacion + 0
    case 3:
        calificacion = calificacion + 0
    case 4:
        calificacion = calificacion + 0
    case _:
        print("opcion no valida.")
        

print("tu calificacion final es:", calificacion)
if calificacion >= 7:
    print("felicidades! aprobaste el examen con", calificacion)
else:
    print("reprobaste el examen con:", calificacion)
