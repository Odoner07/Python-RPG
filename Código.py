import os, time

def Listar_Partidas():
    # Listar los elementos de las partidas
    ruta_partidas = os.listdir(f"{os.getcwd()}/Partidas")

    #Ver las partidas guardadas
    if ruta_partidas:
        print(f"Hay {len(ruta_partidas)} partidas guardadas")
        Ver_partidas = input("¿Quieres ver cuales son?: (Y/N): ")
        
        if Ver_partidas == "Y" or Ver_partidas == "Yes":
            for partida in ruta_partidas:
                print(f"- {partida}")
    else:
        print("No hay partidas guardadas en el directorio actual.")

# Bucle para seleccionar una opción en el menú
while True:
    print("Bienvenido a Python-RPG, que es lo que quieres hacer?: ")
    print("1. Listar las partidas")
    #Selector de opciones
    Opcion = int(input("Quiero: "))
    if Opcion == 1:
        print("")
        Listar_Partidas()
        #Le dice al programa que espere 1.5 segundos
        time.sleep(0.8)
        print("")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")