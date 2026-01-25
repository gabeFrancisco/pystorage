import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "1234",
    database = "pystorage"
)

