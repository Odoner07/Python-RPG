import os, time

# Listar los elementos de las partidas
ruta_partidas = os.path.join(os.getcwd(), "Partidas")

def Listar_Partidas():
    #Si no esta creada la carpeta de partidas la intentara crear
    if not os.path.exists(ruta_partidas):
        print("Ha habido un error y no esta la carpeta de Partidas guardada, vamos a crearla")
        try:
            os.mkdir(ruta_partidas, exist_ok=True)
            print("Ahora ya puedes guardar tus partidas :]")
        except FileExistsError:
            print("La carpeta de partidas ya existe, porque me he ejecutado?")
        except Exception as Error:
            print(f"Ha habido un error en la creación de la carpeta {Error}.")
    #Mira si la carpeta esta creada, en caso afirmativo te deja verlas
    elif os.path.exists(ruta_partidas):
        if len(os.listdir(ruta_partidas)) == 0:
            print("No hay partidas guardadas")
            input("Presiona Enter para continuar...")
        else:
            print(f"Hay {len(os.listdir(ruta_partidas))} partidas guardadas")
            Ver_partidas = input("¿Quieres ver cuales son?: (S/N): ").strip().lower()
            if Ver_partidas in ["s", "si"]:
                for partida in os.listdir(ruta_partidas):
                    print(f"- {partida}")
    #La carpeta existe, pero no hay partidas guardadas
    else:
        print("Error general al listar las partidas")

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
            time.sleep(0.8)
            print("")
        elif Opcion_jugar == 4:
            print("En progreso")
            time.sleep(0.8)
            print("")
        elif Opcion_jugar == 5:
            break
        else:
            print("Opción no válida dentro del menú Jugar.")

# Bucle para seleccionar una opción en el menú
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido a Python-RPG, que es lo que quieres hacer?: ")
    print("1. Jugar")
    print("2. Opciones")
    print("3. Salir")
    
    #Selector de opciones
    try:
        Opcion = int(input("Quiero: "))
    except ValueError:
        print("")
        print("Ponga un numero valido")
        print("")
        continue
        
    if Opcion == 1:
        menu_jugar()
    elif Opcion == 2:
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")