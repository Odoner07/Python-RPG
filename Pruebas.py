import os


# Ruta donde están las partidas
ruta_partidas = "/home/odon/Escritorio/Proyecto-python/Python-RPG/Partidas"

# Listar las partidas
partidas = os.listdir(ruta_partidas)

# Imprimir cada partida de forma individual
for partida in partidas:
    print(partida)
