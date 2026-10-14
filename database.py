import  psycopg2


def connection():
    con=psycopg2.connect(
        host="db",
        user="postgres",
        database="health_file",
        password="password"
    )


    return  con