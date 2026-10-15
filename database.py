import  psycopg2


def connection():
    con=psycopg2.connect(
        host="db",
        user="postgres",
        database="heart",
        password="password",
        port=5432
    )


    return  con