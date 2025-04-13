import os

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

Listar_Partidas()