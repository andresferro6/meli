import flask
import json
from google.cloud import bigquery

bigquery_client = bigquery.Client()

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    query_job = bigquery_client.query(
        """
        SELECT id,
               nombre,
               pais,
               edad,
               ocupacion
        FROM `bold-momentum-346405.pruebaTecnica.pt_clientes_celular`
        """
    ).to_dataframe()
    data_json = query_job.to_json(orient='records')
    print(query_job)
    return json.loads(data_json)