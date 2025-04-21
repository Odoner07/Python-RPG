import time, os
from Python_RPG.Utilidades import ruta_partidas, Listar_Partidas, Eliminar_partida

def menu_jugar():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Empezar partida")
        print("2. Cargar partida")
        print("3. Listar partidas disponibles")
        print("4. Eliminar una partida")
        print("5. Salir al menu anterior")
        try:
            Opcion_jugar = int(input("Quiero: "))
        except ValueError:
            print("")
            print("Ponga un numero valido")
            print("")
            continue

        if Opcion_jugar == 1:
            print("En progreso")
            time.sleep(0.8)
            print("")
        elif Opcion_jugar == 2:
            if os.path.exists(ruta_partidas) and not (len(os.listdir(ruta_partidas)) == 0):
                print("En progreso")
            else:
                print("")
                print("No hay partidas guardadas, revisa el punto 3")
                print("")
                input("Presiona Enter para continuar...")
            print("")
        elif Opcion_jugar == 3:
            print("")
            Listar_Partidas()
            input("Presiona Enter para continuar...")
            print("")
        elif Opcion_jugar == 4:
            Eliminar_partida()
            time.sleep(0.8)
            print("")
        elif Opcion_jugar == 5:
            break
        else:
            print("Opción no válida dentro del menú Jugar.")