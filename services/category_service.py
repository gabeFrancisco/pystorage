from db import connection
from models.category import Category


class CategoryService:
    def getAll(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categories")
            return cursor.fetchall()

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
            print(f"An error occurred: {e}")

            raise e
