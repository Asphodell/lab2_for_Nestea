import shutil
import csv

class DatabaseManager:
    def __init__(self, connection, cursor, name, db):
        self.connection = connection
        self.cursor = cursor
        self.name = name
        self.db = db

    def create_table(self):
        cursor = self.cursor
        connection = self.connection
        name = self.name

        table = f'''
                    CREATE TABLE IF NOT EXISTS {name} (
                    id INTEGER PRIMARY KEY,
                    car TEXT NOT NULL,
                    year INTEGER,
                    price REAL
                    )
                '''

        cursor.execute(table)
        connection.commit()

    def add(self, id, car = None, year = None, price = None):
        connection = self.connection
        cursor = self.cursor
        name = self.name
        try:
            request = f'INSERT INTO {name} VALUES ((?), (?), (?), (?))'

            cursor.execute(request, (id, car, year, price))
            connection.commit()
        except Exception as e:
            print(e)

    def delete(self, id = None, car = None, year = None, price = None):
        connection = self.connection
        cursor = self.cursor
        name = self.name

        cursor.execute(f'DELETE FROM {name} WHERE id = ?', (id,))
        cursor.execute(f'DELETE FROM {name} WHERE car = ?', (car,))
        cursor.execute(f'DELETE FROM {name} WHERE year = ?', (year,))
        cursor.execute(f'DELETE FROM {name} WHERE price = ?', (price,))
        connection.commit()

    def find(self, id = None, car = None, year = None, price = None):
        cursor = self.cursor
        name = self.name

        cursor.execute(f"SELECT * FROM {name} WHERE id = ? OR car = ? OR year = ? OR price = ? ", (id, car, year, price,))

        rows = cursor.fetchall()

        return rows

    def edit(self, id, car = None, year = None, price = None):
        connection = self.connection
        cursor = self.cursor
        name = self.name

        cursor.execute(f'UPDATE {name} SET car = "{car}", year = "{year}", price = "{price}" WHERE id = ?', (id,))
        connection.commit()

    def create_backup(self):
        db = self.db

        shutil.copyfile(db, "backup_" + db)

    def import_to_csv(self):
        cursor = self.cursor
        name = self.name
        db = self.db

        cursor.execute(f"SELECT * FROM {name}")
        with open(f"{db}.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

    def print_table(self):
        cursor = self.cursor
        name = self.name

        select_query = f"SELECT * FROM {name}"

        cursor.execute(select_query)

        rows = cursor.fetchall()

        return rows
