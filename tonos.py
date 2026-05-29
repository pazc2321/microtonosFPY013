import winsound
import time
print("Sintetizador de microtonos")

#Pedir prestados los tonos al computador
maximo_microtonos = 50
microtonos_libres = 50
microtonos_activos = 0
ejecutando = True
while ejecutando:
    print("\n === Panel de microtonos ===")
    print("1. Ver cuántos microtonos quedan libres")
    print("2. Activar microtonos")
    print("3. Devolver microtonos")
    print("4. Monitoriar el estado actual de los microtonos")
    print("5. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        print(f"\n [INFO] Tienes {microtonos_libres} microtonos disponibles para usar")
    elif opcion == 2:
        if microtonos_libres == 0:
            print("No tienes más microtonos disponibles")
        else:
            try:
                cantidad = int(input("¿Cuántos microtonos quieres usar?: "))
                if cantidad <= 0:
                    print("Error: Tienes que activar a lo menos un microtono")
                elif cantidad > microtonos_libres:
                    print(f"Error: No hay tantos microtonos, máximo disponible: {microtonos_libres}")
                else:
                    microtonos_libres -= cantidad
                    microtonos_activos += cantidad
                    #for i in range(1, cantidad + 1):
                    #    print(f"Microtono {i} activado...")
                    #    winsound.Beep(440,300)
                    #    time.sleep(0.8)

                    cancion = [
                        (330, 250), # Mi
                        (294, 250), # Re
                        (523, 500), # Do (Agudo)
                        (392, 500), # Sol
                        (440, 250), # La
                        (523, 500), # Do (Agudo)
                        
                        # --- Frase 2 ---
                        (330, 250), # Mi
                        (294, 250), # Re
                        (523, 500), # Do (Agudo)
                        (392, 500), # Sol
                        (440, 250), # La
                        (523, 750), # Do (Agudo, un poco más larga)
                        
                        # --- Frase 3 (Sube la melodía) ---
                        (330, 250), # Mi
                        (392, 250), # Sol
                        (523, 500), # Do (Agudo)
                        (587, 500), # Re (Agudo)
                        (659, 1000),# Mi (Más agudo aún)
                        (587, 500), # Re (Agudo)
                        (523, 1000),# Do (Agudo)
                        
                        # --- Frase 4 (Baja suavemente) ---
                        (440, 500), # La
                        (523, 500), # Do (Agudo)
                        (587, 500), # Re (Agudo)
                        (523, 500), # Do (Agudo)
                        (494, 1500) # Si
                        #(311,250),(311,250), (311,500),
                        #(311,250),(311,250), (311,500),
                        #(311,250),(370,250),(277,250),(293,250),
                        #(311,1000),
                        #(320,250),(320,250),(320,250),(320,250),
                        #(320,250),(311,250),(311,250),(311,125),(311,125),
                        #(311,250),(293,250),(293,250),(311,255),
                        #(277,500),(429,500)
                    ]
                    for i in range(len(cancion)):
                        frecuencia = cancion[i][0]
                        duracion = cancion[i][1]
                        winsound.Beep(frecuencia,duracion)
                        time.sleep(0.06)
            except ValueError:
                print("Error")
    else:
        print("Error")