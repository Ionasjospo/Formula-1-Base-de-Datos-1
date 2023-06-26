from datetime import datetime

import pymysql
import csv

def insertDataFrom_csv(csv_file):
    # Establece los detalles de conexión a la base de datos
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='bernardo',
        database='F1_Project'
    )
    try:
        # Crea un cursor para ejecutar consultas SQL
        cursor = connection.cursor()

        # Leer el archivo CSV y obtener los datos
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_data = csv.reader(file)
            next(csv_data)  # Omitir la primera fila si contiene encabezados

            # Iterar sobre las filas del archivo CSV e insertar los datos en la tabla
            for row in csv_data:
                # Verificar si la fila no es nula
                row = [None if value == "\\N" else value for value in row]
                # row contiene los valores de cada fila en el archivo CSV
                # Ejemplo de consulta INSERT:
                insert_query = "INSERT INTO races(raceId,year,round,circuitId,name,date,time,url,fp1_date,fp1_time,fp2_date,fp2_time,fp3_date,fp3_time,quali_date,quali_time,sprint_date,sprint_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                values = (row[0], row[1], row[2], row[3], row[4], datetime.strptime(row[5], '%Y-%m-%d').date() if row[5] is not None else None,
                          row[6], row[7], datetime.strptime(row[8], '%Y-%m-%d').date() if row[8] is not None else None, datetime.strptime(row[9], "%H:%M:%S").time() if row[9] is not None else None,
                          datetime.strptime(row[10], '%Y-%m-%d').date() if row[10] is not None else None, datetime.strptime(row[11], "%H:%M:%S").time() if row[11] is not None else None,
                          datetime.strptime(row[12], '%Y-%m-%d').date() if row[12] is not None else None, datetime.strptime(row[13], "%H:%M:%S").time() if row[13] is not None else None,
                          datetime.strptime(row[14], '%Y-%m-%d').date() if row[14] is not None else None,
                          datetime.strptime(row[15], "%H:%M:%S").time() if row[15] is not None else None, datetime.strptime(row[16], '%Y-%m-%d').date() if row[16] is not None else None,
                          datetime.strptime(row[17], "%H:%M:%S").time() if row[17] is not None else None)  # Aquí asume que los valores están en la columna 1 y columna 2
                cursor.execute(insert_query, values)

        # Confirma los cambios en la base de datos
        connection.commit()

    except Exception as e:
        # Maneja cualquier error que ocurra durante la ejecución de consultas
        print("Error:", str(e))
    finally:
        # Cierra el cursor y la conexión a la base de datos
        cursor.close()
        connection.close()
