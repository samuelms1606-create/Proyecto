import datetime
import os

# --- Nombre del archivo para guardar los registros ---
ARCHIVO_REGISTRO = "registro_estudio.txt"

# ----------------------------------------------------------------------
#  FUNCIONES DE UTILIDAD (Cargar/Guardar)
# ----------------------------------------------------------------------

def cargar_registros():
    """Carga todos los registros del archivo de texto."""
    registros = []
    if os.path.exists(ARCHIVO_REGISTRO):
        with open(ARCHIVO_REGISTRO, 'r') as f:
            for linea in f:
                try:
                    # Formato: Asignatura | Fecha | Duracion_minutos
                    asignatura, fecha_str, duracion_str = linea.strip().split(' | ')
                    registros.append({
                        'asignatura': asignatura,
                        'fecha': datetime.datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S'),
                        'duracion_minutos': int(duracion_str)
                    })
                except ValueError:
                    # Ignorar líneas mal formadas
                    continue
    return registros

def guardar_registro(asignatura, duracion_minutos):
    """Guarda una nueva sesión de estudio en el archivo de texto."""
    fecha_actual = datetime.datetime.now()
    # Formato de la línea: Asignatura | Fecha | Duracion_minutos
    linea = f"{asignatura} | {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')} | {duracion_minutos}\n"
    
    with open(ARCHIVO_REGISTRO, 'a') as f:
        f.write(linea)
    print(f"\n Sesión registrada: {asignatura} - {duracion_minutos} minutos.")

# ----------------------------------------------------------------------
#  FUNCIONALIDADES PRINCIPALES
# ----------------------------------------------------------------------

def registrar_sesion():
    """Pide los datos al usuario y guarda la sesión."""
    print("\n---  REGISTRAR NUEVA SESIÓN DE ESTUDIO ---")
    while True:
        asignatura = input("Asignatura estudiada (e.g., Programación, Cálculo): ").strip()
        if asignatura:
            break
        print("La asignatura no puede estar vacía.")

    while True:
        try:
            duracion = int(input("Duración de la sesión en minutos: "))
            if duracion > 0:
                break
            print("La duración debe ser un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            
    guardar_registro(asignatura, duracion)

def mostrar_registros(registros):
    """Muestra todos los registros de estudio cargados."""
    if not registros:
        print("\n No hay registros de estudio aún.")
        return

    print("\n---  HISTORIAL DE SESIONES DE ESTUDIO ---")
    print(f"{'Asignatura':<20} | {'Fecha y Hora':<20} | {'Duración (min)':<15}")
    print("-" * 60)
    for r in registros:
        fecha_formato = r['fecha'].strftime('%Y-%m-%d %H:%M')
        print(f"{r['asignatura']:<20} | {fecha_formato:<20} | {r['duracion_minutos']:<15}")
    print("-" * 60)

def generar_reporte(registros):
    """Calcula y muestra el total de horas por asignatura."""
    if not registros:
        print("\n No hay registros para generar el reporte.")
        return

    print("\n---  REPORTE: HORAS TOTALES POR ASIGNATURA ---")
    total_minutos_por_asignatura = {}
    
    for r in registros:
        # Normalizar el nombre de la asignatura (a minúsculas) para sumar correctamente
        asignatura_key = r['asignatura'].lower().strip()
        total_minutos_por_asignatura[asignatura_key] = (
            total_minutos_por_asignatura.get(asignatura_key, 0) + r['duracion_minutos']
        )
        
    print(f"{'Asignatura':<20} | {'Total Horas':<15} | {'Total Minutos':<15}")
    print("-" * 52)
    
    # Mostrar resultados
    for asignatura, total_minutos in sorted(total_minutos_por_asignatura.items()):
        total_horas = total_minutos / 60
        # Intentar obtener el nombre original de la asignatura para mostrarlo capitalizado
        nombre_mostrar = [r['asignatura'] for r in registros if r['asignatura'].lower().strip() == asignatura][0]
        
        print(f"{nombre_mostrar:<20} | {total_horas:^15.2f} | {total_minutos:^15}")
    print("-" * 52)

# ----------------------------------------------------------------------
#  DOCUMENTACIÓN Y AYUDA (Nuevo Requisito)
# ----------------------------------------------------------------------

def mostrar_descripcion_y_ejemplo():
    """Muestra la descripción de las funcionalidades y un ejemplo de uso."""
    print("\n=============================================")
    print("       AYUDA Y DESCRIPCIÓN DE STUDYBONVENTURIANO      ")
    print("=============================================")
    
    ## DESCRIPCIÓN DE FUNCIONALIDADES
    print("\n###  Funcionalidades Clave")
    print("- **Registro de Sesiones:** Permite guardar la asignatura, la fecha/hora actual, y la duración (en minutos) de cada sesión de estudio.")
    print("- **Persistencia de Datos:** Toda la información se almacena automáticamente en el archivo `registro_estudio.txt` para que no se pierda entre ejecuciones.")
    print("- **Historial Detallado:** Muestra un listado cronológico de todas las sesiones registradas.")
    print("- **Reporte por Asignatura:** Calcula el tiempo total (en horas y minutos) invertido en cada materia, permitiendo analizar la distribución del esfuerzo.")
    
    ## EJEMPLO DE USO
    print("\n###  Ejemplo de Uso")
    print("Imagina que estudias 1 hora y 30 minutos (90 minutos) de Cálculo.")
    print("1. **Selecciona la opción 1** (`Registrar Nueva Sesión de Estudio`).")
    print("2. **Ingresa la asignatura:** `Cálculo Diferencial`")
    print("3. **Ingresa la duración:** `90` (minutos)")
    print("\nMás tarde, estudias 45 minutos de Programación.")
    print("1. **Selecciona la opción 1**.")
    print("2. **Ingresa la asignatura:** `Programación`")
    print("3. **Ingresa la duración:** `45` (minutos)")
    
    print("\nAl seleccionar la **Opción 3** (`Generar Reporte`), el sistema te mostrará:")
    print("```")
    print(f"{'Asignatura':<20} | {'Total Horas':<15}")
    print(f"{'Cálculo Diferencial':<20} | {1.50:^15.2f}")
    print(f"{'Programación':<20} | {0.75:^15.2f}")
    print("```")
    print("\nEsto te ayuda a ver que has invertido el doble de tiempo en Cálculo que en Programación.")

# ----------------------------------------------------------------------
#  FUNCIÓN PRINCIPAL
# ----------------------------------------------------------------------

def menu_principal():
    """Función principal que ejecuta el menú interactivo."""
    while True:
        print("\n=============================================")
        print("            STUDYBONAVENTURIANO           ")
        print("=============================================")
        print("1.  Registrar Nueva Sesión de Estudio")
        print("2.  Ver Historial de Registros")
        print("3.  Generar Reporte de Horas por Asignatura")
        print("4.  Salir")
        print("5.  Ayuda / Descripción de Funcionalidades") # Nueva opción
        print("---------------------------------------------")

        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            registrar_sesion()
        elif opcion == '2':
            registros = cargar_registros()
            mostrar_registros(registros)
        elif opcion == '3':
            registros = cargar_registros()
            generar_reporte(registros)
        elif opcion == '4':
            print("\n¡Gracias por usar StudyBonventuriano! Vuelve pronto para seguir mejorando tu planificación.")
            break
        elif opcion == '5': # Llama a la nueva función de ayuda
            mostrar_descripcion_y_ejemplo()
        else:
            print("\n Opción no válida. Por favor, selecciona un número del 1 al 5.")

# --- Ejecución del programa ---
if __name__ == "__main__":
    menu_principal()
