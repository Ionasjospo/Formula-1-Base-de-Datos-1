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
                # Reemplazar los valores "\N" por None (nulo)
                row = [None if value == "\\N" else value for value in row]

                # row contiene los valores de cada fila en el archivo CSV
                # Ejemplo de consulta INSERT:
                insert_query = "INSERT INTO drivers(driverId,driverRef,number,code," \
                               "forename,surname,dob,nationality,url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                    int(row[0]), row[1], int(row[2]) if row[2] is not None else None, row[3], row[4], row[5], datetime.strptime(row[6], '%Y-%m-%d').date(), row[7], row[8]
                )

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
