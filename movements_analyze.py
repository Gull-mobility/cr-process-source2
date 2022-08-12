def calculate_movements(new_locations,old_locations):
    in_debug = False

    location_with_changes = {}
    movements = []
    counter_new = 0
    counter_change = 0

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
            location_with_changes[plate] = new_locations[plate]
            #Add one to new counter
            counter_new = counter_new + 1
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

                #TODO: Add more conditions like minimum movement or charge
                #TODO: Add a validation if the charge level increease

                #Prepare object of movements and add to list
                movements.append(prepare_movement_object(new_locations[plate], old_locations[plate]))
                
                #Save the change in firestore
                location_with_changes[plate] = new_locations[plate]

                #Add one to change counter
                counter_change = counter_change + 1

    return location_with_changes, movements, counter_new, counter_change

#Build object to save in table 
def prepare_movement_object(new_location, old_location):

    print(new_location)

    movement_object = {
        "city" : new_location['city'],
        "servicio" : new_location['servicio'],
        "idVehiculo" : new_location['idVehiculo'],
        "matricula" : new_location['matricula'],
        "energia_start" : old_location['energia'],
        "energia_end":  new_location['energia'],
        "latitud_start" : old_location['latitud'],
        "latitud_end" : new_location['latitud'],
        "longitud_start" : old_location['longitud'],
        "longitud_end" : new_location['longitud'],
        "tipo" : new_location['tipo'],
        "categoria" : new_location['categoria'],
        "imagen" : new_location['imagen'],
        "uoid_start" : old_location['uoid'],
        "epochTime_start" : old_location['epochTime'],
        "epochTime_end" : new_location['epochTime'],
        "realTime_start" : old_location['realTime'],
        "realTime_end" : new_location['realTime'],
        "geo_start" : old_location['geo'],
        "geo_end" : new_location['geo'],
        #TODO: Add timesamp data
        #ES#"timestamp_start" : old_location['timestamp'],
        "timestamp_end" : new_location['timestamp'],
        "tipoVehiculo" : new_location['tipoVehiculo'],
        "code" : new_location['code'],
        "autonomyValue_start" : old_location['autonomyValue'],
        "autonomyValue_end" : new_location['autonomyValue'],
        "autonomyUnit" : new_location['autonomyUnit'],
        "transmission" : new_location['transmission'],
        "color" : new_location['color'],
        "range" : new_location['range'],
        "fuel" : new_location['fuel'],
        "seats" : new_location['seats'],
        "babySeat" : new_location['babySeat'],
        "boosterSeat" : new_location['boosterSeat'],
        "discounted" : new_location['discounted'],
        "operatingSystemName" : new_location['operatingSystemName'],
        "operationSystemFleetId" : new_location['operationSystemFleetId'],
        "operationSystemVehicleDescriptionId" : new_location['operationSystemVehicleDescriptionId']
    }

    return movement_object