# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:07:55 2022

@author: jferro
"""
import settings
import datetime
import pandas as pd

def clean_clientes(frames: object, config: object):
    """
    Esta función lee un diccionario de dataframes, extrae el dataframe
    de clientes y lleva a cabo un proceso de limpieza de los datos
    
    Parameters
    ----------
    frames : Diccionario
        Diccionario de dataframes, es requerido que tenga la clave Cliente
        Y que como valor contenga el dataframe de Clientes.
    config : Modulo
        Modulo de configuraciones con algunos parametros definidos
        y algunas funciones necesarias para la ejecución del codigo.

    Returns
    -------
    Dataframe: Dataframe limpio con la data.

    """
    frame_clientes = frames.get('Clientes', True)
    frame_clientes.columns = [i.lower().replace(' ', '_') for i in frame_clientes.columns]
    
    frame_clientes['ocupacion'] = frame_clientes['ocupacion'].fillna('NoProporcionado')
    frame_clientes['ocupacion'] = frame_clientes['ocupacion'].replace(config.MAPPER_PROFESIONES_CLIENTE)   
    
    frame_clientes['salario_net_usd'] =  frame_clientes['salario_net_usd'].astype(str).str.replace('ç', '').astype(float)
    
    frame_clientes['estado_civil'] = frame_clientes['estado_civil'].str.strip()
    frame_clientes['estado_civil'] = frame_clientes['estado_civil'].replace(config.MAPPER_ES_CIVIL_CLIENTE)
    
    frame_clientes['genero'] = frame_clientes['genero'].str[:1].str.lower()
    
    frame_clientes['fecha_inactividad'].fillna(datetime.datetime(config.YEAR_ANALISIS, config.MONTH_ANALISIS, config.DAY_ANALISIS), inplace = True)
    frame_clientes['fecha_analisis'] = datetime.datetime(config.YEAR_ANALISIS, config.MONTH_ANALISIS, config.DAY_ANALISIS)
    frame_clientes['dias_inactivo'] = frame_clientes['fecha_analisis'] - frame_clientes['fecha_inactividad']
    frame_clientes['dias_inactivo'] = frame_clientes['dias_inactivo'].dt.days
    
    frame_clientes['score'] = frame_clientes['score'].abs().fillna(frame_clientes['score'].median())
    return frame_clientes

def clean_compras(frames: object):
    frame_compras = frames.get('Compras', True)
    frame_compras.columns = [i.lower().replace(' ', '_') for i in frame_compras.columns]
    frame_compras.columns = [i.lower().replace('(', '') for i in frame_compras.columns]
    frame_compras.columns = [i.lower().replace(')', '') for i in frame_compras.columns]
    return frame_compras

def clean_productos(frames: object):
    frame_productos = frames.get('Producto', True)
    frame_productos.columns = [i.lower().replace(' ', '_') for i in frame_productos.columns]
    frame_productos.columns = [i.lower().replace('(', '') for i in frame_productos.columns]
    frame_productos.columns = [i.lower().replace(')', '') for i in frame_productos.columns]
    return frame_productos
    
if __name__ == '__main__':

    dict_frames = pd.read_excel(settings.RUTA, sheet_name = None)
    frame_clientes = clean_clientes(frames = dict_frames, config = settings)
    frame_compras = clean_compras(frames = dict_frames)
    frame_productos = clean_productos(frames = dict_frames)







