# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:08:03 2022

@author: ASUS
"""
import os
from google.oauth2 import service_account
from google.cloud import bigquery

PROJECT_ID = os.getenv('PROJECT_ID', 'bold-momentum-346405')
DATASET = os.getenv('DATASET', 'pruebaTecnica')
RUTA = os.getenv('RUTA', r"C:\Users\ASUS\Documents\Programacion\pruebasTecnicas\mercadoLibre\meli\data\BBDD.xlsx")
KEYS = os.getenv('KEYS', r"C:\Users\ASUS\Documents\Programacion\pruebasTecnicas\mercadoLibre\meli\data\bold-momentum-346405-0bcf7ffde82a.json")

credentials = service_account.Credentials.from_service_account_file(f'{KEYS}')
client = bigquery.Client(credentials = credentials)
