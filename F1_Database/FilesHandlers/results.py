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
                insert_query = "INSERT INTO results(resultId,raceId,driverId,constructorId,number,grid,position,positionText,positionOrder,points,laps,time,milliseconds,fastestLap,ranking,fastestLapTime,fastestLapSpeed,statusId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


                values = (int(row[0]) if row[0] is not None else None, int(row[1]) if row[1] is not None else None, int(row[2]) if row[2] is not None else None,
                      int(row[3]) if row[3] is not None else None, int(row[4]) if row[4] is not None else None, int(row[5]) if row[5] is not None else None,
                          int(row[6]) if row[6] is not None else None, row[7], int(row[8]) if row[8] is not None else None, float(row[9]) if row[9] is not None else None, int(row[10]) if row[10] is not None else None, row[11], int(row[12]) if row[12] is not None else None, int(row[13]) if row[13] is not None else None, int(row[14]) if row[14] is not None else None,
                          datetime.strptime(row[15], "%M:%S.%f").time() if row[15] is not None else None, row[16], int(row[17]) if row[17] is not None else None)  # Aquí asume que los valores están en la columna 1 y columna 2
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
