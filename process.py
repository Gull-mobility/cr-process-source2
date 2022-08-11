def execution(uoid):
    #Import other clases
    from firestore import firestore_get_old_situation, firestore_write_changes
    from bigquery import bigquery_positions_by_id, bigquery_save_movements
    from movements_analyze import calculate_movements

    #Get last database locations
    old_location = firestore_get_old_situation()
    print('Firestore has ' + str(len(old_location)) + ' vehicles')

    #Get new positions
    new_locations = bigquery_positions_by_id(uoid)
    #Calculate movements
    location_with_changes, movements = calculate_movements(new_locations, old_location)

    #Locantions can be bigger than movements because a new vehicle is not a movements
    print(str(len(location_with_changes)) + ' firestore changes, '  + str(len(movements)) + ' movements')

    #Save movements in bigquery
    bigquery_save_movements(movements)

    #Write in firestore the changes
    firestore_write_changes(location_with_changes)