import os, sys

# Calcula la ruta absoluta del directorio padre de este archivo
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Inserta al inicio de sys.path para que tenga máxima prioridad
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from Python_RPG.Utilidades import ruta_partidas

if len(os.listdir(ruta_partidas)) == 1:
    print(f"Solo hay una partida guardada y es la siguiente:")
    for partida in os.listdir(ruta_partidas):
        print(f"- {partida}")
    while True:
        try:
            Respuesta = str(input("¿Realmente quiere eliminar esta partida? S/N: ")).strip().lower()
        except ValueError:
            print("")
            print("Ponga un caracter valido")
            print("")
            input("Presiona Enter para continuar...")
        if Respuesta == "s":
            # Ruta completa del archivo a borrar
            ruta_archivo = os.path.abspath(os.path.join(ruta_partidas, partida))
            # Verifica que la ruta del archivo esté dentro de la carpeta "Partidas"
            if ruta_archivo.startswith(os.path.abspath(ruta_partidas)) and os.path.isfile(ruta_archivo):
                try:
                    os.remove(ruta_archivo)
                    print(f"Archivo '{partida}' borrado con éxito.")
                except Exception as e:
                    print(f"No se pudo borrar el archivo: {e}")
            else:
                print("Ruta no válida o el archivo no existe.")
            break
        elif Respuesta == "n":
            print("Sabia eleccion, tu partida no ha sido borrada.")
            break
        else:
            print("Diga S (Sí) o N (No)")
elif len(os.listdir(ruta_partidas)) > 1:
    print(f"Hay {len(os.listdir(ruta_partidas))} partidas guardadas y son las siguientes:")
    for partida in os.listdir(ruta_partidas):
        print(f"- {partida}")
    while True:
        Para_eliminar = input("Cual partida quieres eliminar: ")
        # Ruta completa del archivo a borrar
        ruta_archivo = os.path.abspath(os.path.join(ruta_partidas, Para_eliminar))
        # Verifica que la ruta del archivo esté dentro de la carpeta "Partidas"
        if ruta_archivo.startswith(os.path.abspath(ruta_partidas)) and os.path.isfile(ruta_archivo):
            try:
                os.remove(ruta_archivo)
                print(f"Archivo '{Para_eliminar}' borrado con éxito.")
                
                 # Revisamos si ya no quedan más partidas
                if not os.listdir(ruta_partidas):
                    print("")
                    print("Ya no hay más partidas que eliminar.")
                    input("Pulsa Enter para continuar")
                    break
                
                Continuar = input("¿Quiere eliminar otra partida? S/N: ").strip().lower()
                if Continuar == "s":
                    continue
                elif Continuar == "n":
                    break
                else:
                    print("Diga S (Sí) o N (No)")
            except Exception as e:
                print(f"No se pudo borrar el archivo: {e}")
        else:
            print("Ruta no válida o el archivo no existe.")
        break
else:
    print("No hay partidas para eliminar, primero tiene que crear una.")