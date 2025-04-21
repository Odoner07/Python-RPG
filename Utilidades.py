import os

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

def Eliminar_partida():
    if len(os.listdir(ruta_partidas)) == 1:
        print("")
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
                        input("Presiona Enter para continuar...")
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
                print("Ruta no válida o el archivo no existe, fijate bien en el nombre.")
                continue
    else:
        print("")
        print("No hay partidas para eliminar, primero tiene que crear una.")
        input("Presiona Enter para continuar...")