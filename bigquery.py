#Imports bigquery
from google.cloud import bigquery
import datetime

client = bigquery.Client()

#Movements table name
table_id_movements = "vacio-276411.mainDataset.trips_b"

#Get actual positions bigquery for uoid
def bigquery_positions_by_id(uoid):

    print('Query uoid:"' + uoid +'"')

    query = ' '.join(("SELECT * FROM `vacio-276411.mainDataset.bulkData_b`"
                " WHERE uoid = '" + uoid +"'",
                "ORDER BY realTime DESC"))

    query_job = client.query(query)  # Make an API request.

    vehicles = {}
    for row in query_job:
        dictRow = dict(row)

        #Fix some campos that makes problems in fierstore format
        dictRow['energia'] = float(dictRow['energia'])
        dictRow['latitud'] = float(dictRow['latitud'])
        dictRow['longitud'] = float(dictRow['longitud'])
        dictRow['epochTime'] = float(dictRow['epochTime'])
        dictRow['autonomyValue'] = float(dictRow['autonomyValue'])
        dictRow['seats'] = float(dictRow['seats'])

        #Change tipe of timestamp
        dictRow['timestamp'] = datetime.datetime(dictRow['timestamp'].year, dictRow['timestamp'].month, dictRow['timestamp'].day, dictRow['timestamp'].hour, dictRow['timestamp'].minute, dictRow['timestamp'].second)

        vehicles[dictRow['matricula']] = dictRow

    return vehicles


def bigquery_save_movements(movements):

    errors = client.insert_rows_json(table_id_movements, movements)

    #TODO: Change to error loging
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))