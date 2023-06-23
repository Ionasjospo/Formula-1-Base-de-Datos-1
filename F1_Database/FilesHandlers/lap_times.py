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
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file)
            next(csv_data)  # Omitir la primera fila si contiene encabezados

            # Iterar sobre las filas del archivo CSV e insertar los datos en la tabla
            for row in csv_data:
                # Verificar si la fila no es nula
                if all(value is not None for value in row):
                    # row contiene los valores de cada fila en el archivo CSV
                    # Ejemplo de consulta INSERT:
                    insert_query = "INSERT INTO lap_times(raceId,driverId,lap,position," \
                                   "time,milliseconds) VALUES (%s, %s, %s, %s, %s, %s)"

                    rowStr = str(row)  # Parseamos la row
                    rowStr = rowStr.strip("[]")  # Sacamos los "[] "
                    rowStr = rowStr.replace("'", "")
                    attributes = rowStr.split(",")  # Split ";"

                    values = (attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])  # Aquí asume que los valores están en la columna 1 y columna 2
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
