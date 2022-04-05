# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:07:55 2022

@author: ASUS
"""

import datetime
import pandas as pd

def clean_clientes(frames: object, settings: object):
    """
    Esta función lee un diccionario de dataframes, extrae el dataframe
    de clientes y lleva a cabo un proceso de limpieza de los datos
    
    Parameters
    ----------
    frames : Diccionario
        Diccionario de dataframes, es requerido que tenga la clave Cliente
        Y que como valor contenga el dataframe de Clientes.
    settings : Modulo
        Modulo de configuraciones con algunos parametros definidos
        y algunas funciones necesarias para la ejecución del codigo.

    Returns
    -------
    Dataframe: Dataframe limpio con la data.

    """
    
    frame_clientes = dict_frames.get('Clientes', True)
    
    if frame_clientes:
        raise Exception('El Daraframe proporcionado, debe tener le key - Clientes -')
    
    frame_clientes.columns = [i.lower().replace(' ', '_') for i in frame_clientes.columns]
    
    frame_clientes['ocupacion'] = frame_clientes['ocupacion'].fillna('NoProporcionado')
    frame_clientes['ocupacion'] = frame_clientes['ocupacion'].replace(settings.MAPPER_PROFESIONES_CLIENTE)   
    
    frame_clientes['salario_net_usd'] =  frame_clientes['salario_net_usd'].astype(str).str.replace('ç', '').astype(float)
    
    frame_clientes['estado_civil'] = frame_clientes['estado_civil'].str.strip()
    frame_clientes['estado_civil'] = frame_clientes['estado_civil'].replace(settings.MAPPER_ES_CIVIL_CLIENTE)
    
    frame_clientes['genero'] = frame_clientes['genero'].str[:1].str.lower()
    
    frame_clientes['fecha_inactividad'].fillna(datetime.datetime(settings.YEAR_ANALISIS, settings.MONTH_ANALISIS, settings.DAY_ANALISIS), inplace = True)
    frame_clientes['fecha_analisis'] = datetime.datetime(settings.YEAR_ANALISIS, settings.MONTH_ANALISIS, settings.DAY_ANALISIS)
    frame_clientes['years_inactivo'] = frame_clientes['fecha_analisis'] - frame_clientes['fecha_inactividad']
    frame_clientes['years_inactivo'] = frame_clientes['years_inactivo'].dt.days / 365
    
    frame_clientes['score'] = frame_clientes['score'].abs().fillna(frame_clientes['score'].median())
    return frame_clientes


if __name__ == '__main__':
    import settings
    dict_frames = pd.read_excel(settings.RUTA, sheet_name = None)
    clean_clientes(dict_frames, )
    frame_compras = dict_frames.get('Compras')
    frame_productos = dict_frames.get('Producto')







