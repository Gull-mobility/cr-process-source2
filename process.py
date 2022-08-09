def execution(uoid):
    #Import other clases
    from firestore import firestore_get_old_situation, firestore_write_changes
    from bigquery import bigquery_positions_by_id
    from movements_analyze import calculate_movements

    #Get last database locations
    dict_old_location = firestore_get_old_situation()
    print('Firestore has ' + str(len(dict_old_location)) + ' vehicles')

    #Get new positions
    new_locations = bigquery_positions_by_id(uoid)
    #Calculate movements
    changes = calculate_movements(new_locations)

    #Write in firestore the changes
    firestore_write_changes(changes)