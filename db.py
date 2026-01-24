from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "pystorage"
)

