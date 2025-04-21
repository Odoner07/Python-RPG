import os, sys

# Calcula la ruta absoluta del directorio padre de este archivo
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Inserta al inicio de sys.path para que tenga máxima prioridad
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    
# ¡No mover de sitio o dara lugar a error!
from Python_RPG.Menus.Menu_jugar import menu_jugar

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
        print("")
        print("En progreso")
        input("Presiona Enter para continuar...")
        print("")
    elif Opcion == 3:
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")