from db import connection
from models.category import Category
from datetime import datetime


class CategoryRepository:
    def getAll(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categories ORDER BY created_at")
            rows = cursor.fetchall()

            categories = []

            for row in rows:
                category = Category(
                    id=row[0], created_at=row[1], updated_at=row[2], name=row[3]
                )
                categories.append(category)

        return categories

    def get(self, id: int):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM categories WHERE id = %s""", (id,))
                rows = cursor.fetchall()

            for row in rows:
                category = Category(
                    id=row[0], created_at=row[1], updated_at=row[2], name=row[3]
                )

            return category

        except Exception as e:
            connection.rollback()

            raise e

    def create(self, category: Category):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO categories(created_at, name) values (
                        %s, %s
                    )""",
                    (
                        category.created_at,
                        category.name,
                    ),
                )

            connection.commit()
            print("Product created succesfully!")

        except Exception as e:
            connection.rollback()

            raise e

    def update(self, category: Category):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE categories set updated_at = %s, name = %s where id = %s
                    """,
                    (datetime.now(), category.name, category.id),
                )

                connection.commit()
        except Exception as e:
            connection.rollback()
            raise e

    def delete(self, id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM categories WHERE id = %s""", (id,))
                connection.commit()
        except Exception as e:
            connection.rollback()

            raise e
