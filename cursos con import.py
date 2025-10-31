from CURSOSCORREGIDO import cursos
from CURSOSCORREGIDO import alumnos_por_curso
from CURSOSCORREGIDO import maestros
from CURSOSCORREGIDO import aulas

def mostrar_cursos():
    print("\nCursos disponibles:")
    for i, c in enumerate(cursos, start=1):
        print(f"{i}. {c}")

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
4. Eliminar alumno de curso
5. Eliminar curso
6. Agregar curso
7. Salir
Seleccione una opción: """).strip()

        if des == "1":
            mostrar_cursos()
            info_curso = input("Seleccione el número del curso: ").strip()
            if info_curso.isdigit() and 1 <= int(info_curso) <= len(cursos):
                index = int(info_curso) - 1
                curso = cursos[index]
                print(f"\nCurso: {curso}")
                print(f"Maestro: {maestros[index]}")
                print(f"Aula: {aulas[index]}")
                print(f"Alumnos: {alumnos_por_curso.get(curso, [])}")
            else:
                print("Opción de curso inválida.")

        elif des == "2":
            mostrar_cursos()
            curso_cambiar = input("Seleccione el número del curso: ").strip()
            if curso_cambiar.isdigit() and 1 <= int(curso_cambiar) <= len(cursos):
                index = int(curso_cambiar) - 1
                nuevo_maestro = input(f"Ingrese el nombre del nuevo maestro para {cursos[index]}: ").strip()
                maestros[index] = nuevo_maestro
                print(f"El maestro del curso {cursos[index]} ahora es {nuevo_maestro}.")
            else:
                print("Opción de curso inválida.")

        elif des == "3":
            mostrar_cursos()
            curso_incorporar = input("Seleccione el número del curso: ").strip()
            if curso_incorporar.isdigit() and 1 <= int(curso_incorporar) <= len(cursos):
                index = int(curso_incorporar) - 1
                curso = cursos[index]
                nuevo_alumno = input("Ingrese el nombre del nuevo alumno: ").strip()
                alumnos_por_curso.setdefault(curso, []).append(nuevo_alumno)
                print(f"El alumno {nuevo_alumno} ha sido incorporado al curso {curso}.")
            else:
                print("Opción de curso inválida.")

        elif des == "4":
            mostrar_cursos()
            curso_eliminar = input("Seleccione el número del curso: ").strip()
            if curso_eliminar.isdigit() and 1 <= int(curso_eliminar) <= len(cursos):
                index = int(curso_eliminar) - 1
                curso = cursos[index]
                print(f"Alumnos actuales en {curso}: {alumnos_por_curso.get(curso, [])}")
                alumno_eliminar = input("Ingrese el nombre del alumno a eliminar: ").strip()
                if alumno_eliminar in alumnos_por_curso.get(curso, []):
                    alumnos_por_curso[curso].remove(alumno_eliminar)
                    print(f"El alumno {alumno_eliminar} ha sido eliminado del curso {curso}.")
                else:
                    print(f"El alumno {alumno_eliminar} no está inscrito en el curso {curso}.")
            else:
                print("Opción de curso inválida.")

        elif des == "5":
            mostrar_cursos()
            curso_borrar = input("Seleccione el número del curso: ").strip()
            if curso_borrar.isdigit() and 1 <= int(curso_borrar) <= len(cursos):
                index = int(curso_borrar) - 1
                curso_eliminado = cursos.pop(index)
                maestros.pop(index)
                aulas.pop(index)
                alumnos_por_curso.pop(curso_eliminado, None)
                print(f"El curso '{curso_eliminado}' ha sido eliminado correctamente.")
            else:
                print("Opción de curso inválida.")

        elif des == "6":
            nuevo_curso = input("Ingrese el nombre del nuevo curso: ").strip()
            nuevo_maestro = input("Ingrese el nombre del maestro del nuevo curso: ").strip()
            nueva_aula = input("Ingrese el número del aula del nuevo curso: ").strip()
            cursos.append(nuevo_curso)
            maestros.append(nuevo_maestro)
            aulas.append(int(nueva_aula))
            alumnos_por_curso[nuevo_curso] = []
            print(f"El curso '{nuevo_curso}' ha sido agregado correctamente.")

        elif des == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para volver al menú...")

gestion_cursos()