from db import connection
from models.product import Product


class ProductService:
    db = None

    def getAll(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            return cursor.fetchall()

    def create(self, product: Product):
        try:
            with connection.cursor() as cursor:
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
                print("Product created succesfully!")
        except Exception as e:
            connection.rollback()
            print(f"An error occurred: {e}")

            raise e

    def get(self, id: int):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM products WHERE id = %s""", id)
                return cursor.fetchall()
        except Exception as e:
            connection.rollback()
            print(f"An error occurred: {e}")

            raise e

    def getTotal(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT SUM(price) FROM products")
                return cursor.fetchall()
        except Exception as e:
            connection.rollback()
            print(f"An error occurred: {e}")

            raise e
