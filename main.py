from librerias.estadisticas import cargar_datos, mostrar_estadisticas

# Ruta del CSV dentro de tu carpeta datos/
RUTA_CSV = "data/data.csv"

def menu():
    # Cargamos los datos una sola vez
    datos = cargar_datos(RUTA_CSV)

    # Mostramos el menú principal
    # While lo dejo en True para que el menú se repita hasta que el usuario decida salir

    while True:
        print("1. Mostrar estadísticas de Lionel Messi")
        print("2. Mostrar estadísticas de Cristiano Ronaldo")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_estadisticas("Lionel Messi", datos)

        elif opcion == "2":
            mostrar_estadisticas("Cristiano Ronaldo", datos)

        elif opcion == "3":
            print(" ---  ¡¡¡Ciao!!!  --- ")
            break

        else:
            print("Opción no existe wey :) \n")


# Aquí lo de ejecutar el menú
menu()
