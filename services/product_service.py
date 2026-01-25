from db import connection
from models.product import Product


class ProductService:
    db = None

    def getAll(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")

        result = cursor.fetchall()

        connection.commit()
        connection.close()

        return result

    def create(self, product: Product):
        try:

            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO products(created_at, name, description, quantity, price) values (
                    %s, %s, %s, %s, %s           
                )""",
                (
                    product.created_at,
                    product.name,
                    product.description,
                    product.quantity,
                    product.price,
                ),
            )

            # result = cursor.fetchall()

            connection.commit()
            connection.close()

            print("Product created succesfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
