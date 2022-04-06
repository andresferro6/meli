# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:02:26 2022

@author: ASUS
"""

import settings
import extract as ex
import pandas as pd

dict_frames = pd.read_excel(settings.RUTA, sheet_name = None)
frame_clientes = ex.clean_clientes(frames = dict_frames, config = settings)
frame_compras = ex.clean_compras(frames = dict_frames)
frame_productos = ex.clean_productos(frames = dict_frames)

frame_clientes.to_gbq(destination_table = settings.NOMBRE_TABLA_CLIENTE,
                      project_id = settings.PROJECT_ID,
                      credentials = settings.credentials,
                      if_exists = settings.IF_EXIST )

frame_compras.to_gbq(destination_table = settings.NOMBRE_TABLA_COMPRAS,
                      project_id = settings.PROJECT_ID,
                      credentials = settings.credentials, 
                      if_exists = settings.IF_EXIST )

frame_productos.to_gbq(destination_table = settings.NOMBRE_TABLA_PRODUCTOS,
                      project_id = settings.PROJECT_ID,
                      credentials = settings.credentials, 
                      if_exists = settings.IF_EXIST )