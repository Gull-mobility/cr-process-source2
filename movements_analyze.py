def calculate_movements(new_locations,old_locations):
    in_debug = False

    changes = {}

    #Para todas las nuevas posiciones comparamos con posicion anterior
    for plate in new_locations:
        print('[FUNC]check_movements') if in_debug else ''

        print('dict_old_locations:') if in_debug else ''
        print(old_locations) if in_debug else ''

        #Esto ya no haria falta, guardar al final
        #Check if plate exist in firebase database
        if plate not in old_locations.keys():
            print('[check_movements]New vehicle') if in_debug else ''
            print(new_locations) if in_debug else ''
            #If this vehicule do not exist not continue

            #Si es nueva la anadimos a firestore
            changes[plate] = new_locations[plate]
        else:

            new_latitude = new_locations[plate]['latitud']
            old_latitude = old_locations[plate]['latitud']

            new_longitude = new_locations[plate]['longitud']
            old_longitude = old_locations[plate]['longitud']

            if(new_latitude == old_latitude and new_longitude == old_longitude):
                print('[check_movements] Son iguales') if in_debug else ''
            else:
                print('[check_movements] Son distintas') if in_debug else ''
                print(new_latitude, old_latitude, new_longitude, old_longitude) if in_debug else ''

                #Si son distintas hay que enviar a bigquery - TODO
                
                #Solo guardamos el cambio
                changes[plate] = new_locations[plate]

    return changes