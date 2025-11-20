import datetime

ARCHIVO = "registros.txt"

def registrar():
    materia = input("Materia: ")
    fecha = input("Fecha (YYYY-MM-DD) o Enter para hoy: ")

    if fecha == "":
        fecha = str(datetime.date.today())

    horas = input("Horas estudiadas: ")

    linea = materia + "," + fecha + "," + horas + "\n"

    with open(ARCHIVO, "a") as f:
        f.write(linea)

    print("\n✔ Registro guardado.\n")


def total_por_materia():
    totales = {}

    try:
        with open(ARCHIVO, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                materia = datos[0]
                horas = float(datos[2])

                if materia in totales:
                    totales[materia] += horas
                else:
                    totales[materia] = horas

    except FileNotFoundError:
        print("No hay registros aún.\n")
        return

    print("\n--- Total de horas por materia ---")
    for m, h in totales.items():
        print(m, ":", h, "horas")
    print()


def total_semana():
    hoy = datetime.date.today()
    semana_actual = hoy.isocalendar().week
    total = 0

    try:
        with open(ARCHIVO, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                fecha = datetime.datetime.strptime(datos[1], "%Y-%m-%d").date()
                horas = float(datos[2])

                if fecha.isocalendar().week == semana_actual:
                    total += horas

    except FileNotFoundError:
        print("No hay registros aún.\n")
        return

    print("\nHoras estudiadas esta semana:", total, "\n")


def menu():
    while True:
        print("==== StudyBonaventuriano ====")
        print("1. Registrar sesión de estudio")
        print("2. Ver total por materia")
        print("3. Ver total semana actual")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar()
        elif opcion == "2":
            total_por_materia()
        elif opcion == "3":
            total_semana()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")


menu()
