from db import connection


class InfoRepository:
    def getDbSize(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT pg_database_size('pystorage');")

                size = cursor.fetchone()[0]

                cursor.close()
                connection.close()

                return size
        except Exception as e:
            print("Error getting database size!")
            return None
