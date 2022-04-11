# Meli - Mercado Libre
Este repositorio contiene la prueba técnica de mercado libre para el cargo de Analista Senior de Datos

# Pasos para configurar IAM - BigQuery

- 1: Creación de la cuenta de servicios en iam de gcp.  **Esto nos dará las claves de acceso a GCP**
- 2: Otorgamos los permisos 1.1 Administrador de BigQuery y 1.2 Usuario de trabajo de BigQuery
- 3: Creamos la llaves en formato JSON y exportamos. **Ponerlas en una ruta segura, por la prueba**
     irán dentro del Repo, sin embargo, ponerlo en una ruta local o variable de entorno}
- 4: Entramos a BigQuery, aprovisionamos un proyecto y un dataset para la creación de la prueba. 
- 5. Para este caso puntual proyecto: **_meli-analista-senior_**, dataset: **_pruebaTecnica_**

Para ver la documentación de Google sobre IAM: [https://cloud.google.com/iam?hl=es-419](url)

# Datos:

- 1: Se resuelve la prueba teniendo en cuenta dos enfoques, ETL (Extract, Transform, Load) y ELT (Extract, Load, Tranform)
- 2: Enfoque de la prueba Serveless
- 3: El backend de la prueba fue desarrollado en BigQuery, Cloud Funcitons, Cloud Storage. El lenguje empleado fue Python.
- 4: Cada ambiente esta aislado con su propio requierents.txt
- 5: Para ver a creación del reporte: ver carpeta report
- 6: Para ver la creaciónd el front: ver carpeta docs
- 7: Para ver la creación de la api: ver carpeta apis
- 8: Para ver la tranfcormación de los archivos, revisar los archivos .py.