import csv

# ---------------------------------------------------------
# Cargar todos los datos del CSV y devolverlos como lista
# ---------------------------------------------------------
def cargar_datos(ruta_csv):
    datos = []

    # Se abre el fichero CSV
    with open(ruta_csv, encoding="utf-8") as fichero:
        lector = csv.DictReader(fichero)

        # Cada fila del CSV se convierte en un diccionario
        for fila in lector:
            datos.append(fila)

    return datos


# función para contar partidos por competición

def partidos_por_competicion(datos, jugador):
    partidos = {}

    for fila in datos:
        if fila["Player"] == jugador:

            competicion = fila["Competition"]

            # Clave única del partido:
            # Fecha + Rival + Competición
            clave = (fila["Date"], fila["Opponent"], fila["Competition"])

            # Si la competición no existe aún, la creamos
            if competicion not in partidos:
                partidos[competicion] = set()

            # Añadimos el partido al set (evita duplicados)
            partidos[competicion].add(clave)

    # Convertimos sets → números
    resumen = {comp: len(partidos[comp]) for comp in partidos}
    return resumen



# Mostrar estadísticas en pantalla

def mostrar_estadisticas(jugador, datos):
    print("===== ESTADÍSTICAS =====")
    print(f"Jugador: {jugador}\n")
    print("Partidos por competición:")

    stats = partidos_por_competicion(datos, jugador)

    # Imprimir cada competición con su número de partidos

    for comp, num in stats.items():
        print(f"- {comp}: {num}")
