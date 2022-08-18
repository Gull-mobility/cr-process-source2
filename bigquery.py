#Imports bigquery
from google.cloud import bigquery
import datetime

client = bigquery.Client()

#Movements table name
table_id_movements = "vacio-276411.mainDataset.trips_b"

#Get actual positions bigquery for uoid
def bigquery_positions_by_id(uoid, date_first, date_end):

    print('Query uoid:"' + uoid +'"')

    query = ' '.join(("SELECT * FROM `vacio-276411.mainDataset.bulkData_b`"
                "WHERE DATE(timestamp) BETWEEN '" + date_first  + "' AND '" + date_end  + "'",
                "AND uoid = '" + uoid +"'"))

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

        vehicles[dictRow['matricula']] = dictRow

    return vehicles


def bigquery_save_movements(movements):

    errors = client.insert_rows_json(table_id_movements, movements)

    #TODO: Change to error loging
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))


#This function is only used by bulk class, not in production execution
def bigquery_bulk_uoid():



  #Done
  # "2022-06-01" AND  "2022-08-17"
  query = """
      SELECT uoid, timestamp  FROM `vacio-276411.mainDataset.bulkData_b` 
      WHERE DATE(timestamp) BETWEEN "2022-08-18" AND  "2022-08-18"
      GROUP BY uoid, timestamp
      ORDER BY timestamp ASC
  """

  query_job = client.query(query)  # Make an API request.



  list_uoids = []
  for row in query_job:
      #print("name={}".format(row[0]))
      list_uoids.append(row)

  return list_uoids