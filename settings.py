# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:08:03 2022

@author: ASUS
"""
import os
from google.oauth2 import service_account
from google.cloud import bigquery

PROJECT_ID = os.getenv('PROJECT_ID', 'meli-analista-senior')
DATASET = os.getenv('DATASET', 'pruebaTecnica')
RUTA = os.getenv('RUTA', r"C:\Users\ASUS\Documents\Programacion\pruebasTecnicas\mercadoLibre\meli\data\BBDD.xlsx")
KEYS = os.getenv('KEYS', r"C:\Users\ASUS\Documents\Programacion\pruebasTecnicas\mercadoLibre\meli\data\meli-analista-senior-4fa84e025cf7.json")

credentials = service_account.Credentials.from_service_account_file(f'{KEYS}')
client = bigquery.Client(credentials = credentials)

YEAR_ANALISIS = 2022
MONTH_ANALISIS = 4
DAY_ANALISIS = 4

MAPPER_PROFESIONES_CLIENTE = {'in dependiente': 'Independiente', 
                              'emp': 'Empleado',
                              'Soltero': 'NoProporcionado'}

MAPPER_ES_CIVIL_CLIENTE = {'Cas': 'Casado', 
                           'Sol': 'Soltero',
                           'Cosado': 'Casado'}
