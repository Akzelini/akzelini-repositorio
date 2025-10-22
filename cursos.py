cursos = ["Diseño de modas", "Canto", "Programación", "Trading", "Pintura"]
maestros = ["Ana", "Carlos", "Luisa", "Miguel", "Sofía"]
aulas = [101, 202, 303, 404, 505]
alumnos = ["Jorge", "Lucía", "Pedro", "Elena", "Andrés", "Sofía", "Diego", "Valentina",
           "Camila", "Martín", "Laura", "Fernando","Gabriela", "Ricardo", "Isabela", 
           "Santiago", "Natalia", "Andrés", "Laura", "Diego", "Valentina", "Rumina",
           "Zoe", "Luna", "Coco"]

def gestion_cursos():
    print("=== Bienvenido a la gestión de cursos ===")
    yn = input("¿Desea iniciar? (1. sí / 2. no): ").strip()

    if yn != "1":
        print("Saliendo del sistema...")
        return

    while True:
        des = input("""
¿Qué desea hacer?
1. Información del curso
2. Cambiar maestro de curso
3. Incorporar alumno a curso
4. Salir
Seleccione una opción: """)

        if des == "1":
            info_curso = input("""¿Qué curso desea consultar? (1-5)
1. Diseño de modas
2. Canto
3. Programación
4. Trading
5. Pintura
Seleccione: """)
            if info_curso in ["1","2","3","4","5"]:
                index = int(info_curso) - 1
                start = index*5
                end = start + 5
                print(f"\nCurso: {cursos[index]}")
                print(f"Maestro: {maestros[index]}")
                print(f"Aula: {aulas[index]}")
                print(f"Alumnos: {alumnos[start:end]}")
            else:
                print("Opción de curso inválida.")

        elif des == "2":
            curso_cambiar = input("""¿A qué curso desea cambiar el maestro? (1-5)
1. Diseño de modas
2. Canto
3. Programación
4. Trading
5. Pintura
Seleccione: """)
            if curso_cambiar in ["1","2","3","4","5"]:
                index = int(curso_cambiar) - 1
                nuevo_maestro = input(f"Ingrese el nombre del nuevo maestro para {cursos[index]}: ").strip()
                maestros[index] = nuevo_maestro
                print(f"El maestro del curso {cursos[index]} ahora es {nuevo_maestro}.")
            else:
                print("Opción de curso inválida.")

        elif des == "3":
            curso_incorporar = input("""¿A qué curso desea incorporar un alumno? (1-5)
1. Diseño de modas
2. Canto
3. Programación
4. Trading
5. Pintura
Seleccione: """)
            if curso_incorporar in ["1","2","3","4","5"]:
                nuevo_alumno = input("Ingrese el nombre del nuevo alumno: ").strip()
                alumnos.append(nuevo_alumno)
                index = int(curso_incorporar) - 1
                print(f"El alumno {nuevo_alumno} ha sido incorporado al curso {cursos[index]}.")
            else:
                print("Opción de curso inválida.")

        elif des == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para volver al menú...")

gestion_cursos()
