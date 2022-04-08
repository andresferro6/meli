import json
import flask
from settings import client

app = flask.Flask(__name__)

# https://us-central1-bold-momentum-346405.cloudfunctions.net/api-meli-prueba-tecnica

@app.route("/")
def hello_world():
    if not flask.request.args.get('table'):
        return {'status': 400,
                'mensaje':'There"s no table to query',
        }
    query = f"""
                SELECT *
                FROM `bold-momentum-346405.pruebaTecnica.{flask.request.args.get('table')}` t1
                """ 
    query_job = client.query(query).to_dataframe()
    data_json = query_job.to_json(orient='records')
    return data_json