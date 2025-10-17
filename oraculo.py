from datetime import datetime

def calcular_elemento(fecha_nacimiento):
    año = int(fecha_nacimiento)
    match (año % 10):
        case 0 | 1:
            return "tierra"
        case 2 | 3:
            return "agua"
        case 4 | 5:
            return "fuego"
        case 6 | 7:
            return "aire"
        case 8 | 9:
            return "espiritu"

def generar_prediccion(nombre, numero_suerte, edad, elemento):
    match numero_suerte:
        case 1:
            return f"{nombre}, este año traerá muchos cambios. Usa tu energía de {elemento} para adaptarte y avanzar."
        case 2:
            return f"{nombre}, la paciencia será importante este año. Tu elemento {elemento} te ayudará a mantener el equilibrio."
        case 3:
            return f"{nombre}, la creatividad te ayudará a superar los desafíos. Confía en la fuerza de tu elemento {elemento}."
        case 4:
            return f"{nombre}, este año será ideal para fortalecer tus relaciones personales. Deja que la energía de {elemento} te guíe."
        case _:
            return f"{nombre}, el número que elegiste no es válido. Debe ser del 1 al 4."

def iniciar_oraculo():
    while True:
        opcion = input("quieres saber tu suerte? (si/no): ").lower()
        if opcion == "no":
            print("cerrando oraculo...")
            break

        nombre = input("como te llamas: ")
        fecha_nacimiento = input("en que año naciste: ")
        numero_suerte = int(input("dime un numero del 1 al 4: "))

        edad = datetime.now().year - int(fecha_nacimiento)
        elemento = calcular_elemento(fecha_nacimiento)
        prediccion = generar_prediccion(nombre, numero_suerte, edad, elemento)

        print("\n" + "*" * 30)
        print("oraculo en python")
        print(f"edad: {edad} años")
        print(f"elemento: {elemento}")
        print(prediccion)
        print("*" * 30 + "\n")

iniciar_oraculo()
