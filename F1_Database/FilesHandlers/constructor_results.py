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
                row = [None if value == "\\N" else value for value in row]
                # row contiene los valores de cada fila en el archivo CSV
                # Ejemplo de consulta INSERT:
                insert_query = "INSERT INTO constructor_results(constructorResultsId,raceId," \
                                   "constructorId,points,status) VALUES (%s, %s, %s, %s, %s)"

                values = (row[0], row[1], row[2], row[3], row[4])  # Aquí asume que los valores están en la columna 1 y columna 2
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
