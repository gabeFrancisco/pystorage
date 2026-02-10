from db import connection
from models.product import Product
from models.dtos.product_dto import ProductDTO


class ProductRepository:
    def getAll(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    p.id,
                    p.created_at,
                    p.updated_at,
                    p.name,
                    p.description,
                    p.quantity,
                    p.price,
                    c.name as category
                FROM
                    products p
                    INNER JOIN categories c ON p.category_id = c.id
                    ORDER BY created_at;
                """
            )

            rows = cursor.fetchall()

            products = []

            for row in rows:
                product = ProductDTO(
                    id=row[0],
                    created_at=row[1],
                    updated_at=row[2],
                    name=row[3],
                    description=row[4],
                    quantity=row[5],
                    price=row[6],
                    category=row[7],
                )

                products.append(product)

        return products

    def create(self, product: Product):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO products(created_at, name, description, quantity, price, category_id) values (
                        %s, %s, %s, %s, %s, %s          
                    )""",
                    (
                        product.created_at,
                        product.name,
                        product.description,
                        product.quantity,
                        product.price,
                        product.category_id,
                    ),
                )

            connection.commit()
        except Exception as e:
            connection.rollback()

            raise e

    def get(self, id: int):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM products WHERE id = %s""", id)
                return cursor.fetchall()
        except Exception as e:
            connection.rollback()

            raise e

    def getTotal(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT SUM(price) FROM products")
                return cursor.fetchall()
        except Exception as e:
            connection.rollback()

            raise e

    def delete(self, id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM products WHERE id = %s""", id)
                connection.commit()
        except Exception as e:
            connection.rollback()

            raise e
