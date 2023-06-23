import pymysql
def connection(host, user, password, database):
    # Establece los detalles de conexión a la base de datos
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )