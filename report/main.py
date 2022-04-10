import settings
import pandas as pd
from pandas_profiling import ProfileReport

query = f"""
    SELECT  
        id,
        cust_id,
        prod_id,
        cast(gasto as string) as GASTO,
        --fechacompra,
        nombre_producto,
        valor_producto,
        cantidad_datos_gb_prod,
        vigencia_dias_producto,
        nombre,
        pais,
        edad,
        ocupacion,
        score,
        salario_net_usd,
        estado_civil,
        estado,
        fecha_inactividad,
        genero,
        device,
        nivel_educativo,
        carrera,
        dias_inactivo,
        --fecha_analisis,
        nombre_fill,
        dias_vs_ultima_compra,
        life_time_value 
    FROM `{settings.PROJECT_ID}.{settings.DATASET}.pt_master_table_etl`
"""
frame = settings.client.query(query).to_dataframe()
frame['mmmm'] = frame['GASTO'].astype(float)
frame['mmmm_DOS'] = [float(x) for x in frame['GASTO']]
frame['mmmm_TRES'] = [int(x) for x in frame['GASTO']]

profile = ProfileReport(frame, 
                        title = "Prueba Técnica Meli"
                        )
profile.to_file("report.html")


