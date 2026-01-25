from db import connection

class ProductService:
    db = None

    def getAll(self):
        conn = connection.cursor();
        conn.execute("SELECT * FROM products")
        
        result = conn.fetchall();

        connection.commit()
        connection.close()

        return result; 