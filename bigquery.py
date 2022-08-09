#Imports bigquery
from google.cloud import bigquery

client = bigquery.Client()

#Get actual positions bigquery for uoid
def bigquery_positions_by_id(uoid):

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

    vehicles[dictRow['matricula']] = dictRow

  return vehicles