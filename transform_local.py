# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:39:41 2022

@author: ASUS
"""
import numpy as np
import settings
import extract as ex
import pandas as pd
from pandasql import sqldf

dict_frames = pd.read_excel(settings.RUTA, sheet_name = None)
frame_clientes = ex.clean_clientes(frames = dict_frames, config = settings)
frame_compras = ex.clean_compras(frames = dict_frames)
frame_productos = ex.clean_productos(frames = dict_frames)

query = """
    SELECT t1.id,
           t1.cust_id,
           t1.prod_id,
           t1.gasto,
           t1.fechacompra,
           t2.nombre as nombre_producto,
           t2.valor as valor_producto,
           t2.cantidad_datos_gb as cantidad_datos_gb_prod,
           t2.vigencia_dias as vigencia_dias_producto  ,
           t3.nombre,
           t3.pais,
           t3.edad,
           t3.ocupacion,
           t3.score,
           t3.salario_net_usd,
           t3.estado_civil,
           t3.estado,
           t3.fecha_inactividad,
           t3.genero,
           t3.device,
           t3.nivel_educativo,
           t3.carrera,
           t3.dias_inactivo,
           t3.fecha_analisis
    FROM frame_compras t1
    LEFT JOIN frame_productos t2
    ON t1.prod_id = t2.id
    LEFT JOIN frame_clientes t3
    ON t1.cust_id = t3.id
"""
result_frame = sqldf(query)

result_frame['fechacompra'] = pd.to_datetime(result_frame['fechacompra'])
result_frame['fecha_inactividad'] = pd.to_datetime(result_frame['fecha_inactividad'])
result_frame['fecha_analisis'] = pd.to_datetime(result_frame['fecha_analisis'])
result_frame['nombre_fill'] = result_frame['cust_id'].apply(lambda x: f'c{x}')

for column in result_frame.columns:
    
    if result_frame[f'{column}'].dtype == '<M8[ns]':
        result_frame[f'{column}'].fillna(result_frame[f'{column}'].max(), inplace = True) 
    elif (result_frame[f'{column}'].dtype == 'float64') or (result_frame[f'{column}'].dtype == 'int64'):
        result_frame[f'{column}'].fillna(result_frame[f'{column}'].median(), inplace = True) 
    else:
        result_frame[f'{column}'].fillna(result_frame[f'{column}'].mode()[0], inplace = True) 

result_frame['dias_vs_ultima_compra'] = result_frame['fecha_analisis'] - result_frame['fechacompra']  
result_frame['dias_vs_ultima_compra'] = result_frame['dias_vs_ultima_compra'].dt.days
result_frame['life_time_value'] = result_frame['dias_vs_ultima_compra'] - result_frame['dias_inactivo']
result_frame['life_time_value'] = np.where(result_frame['dias_inactivo'] == 0, 0, result_frame['life_time_value'])


result_frame['estado'] = result_frame['estado'].replace({1: 'activo', 0: 'inactivo'}) 

result_frame.to_gbq(destination_table = f'{settings.DATASET}.pt_master_table_etl',
                       project_id = settings.PROJECT_ID,
                       credentials = settings.credentials, 
                       if_exists = settings.IF_EXIST )
