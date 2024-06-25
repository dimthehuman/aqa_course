from context_manager import DBManager


def create_products_table():
    with DBManager("shop.db") as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    price REAL NOT NULL,
                                    quantity INTEGER NOT NULL)''')
        cursor.connection.commit()


def add_data_to_products_table():
    create_products_table()
    with DBManager("shop.db") as cursor:
        products = [("Orange", 0.5, 100),
                    ("Apple", 0.3, 200),
                    ("Banana", 0.2, 150)]

        for product in products:
            cursor.execute('''INSERT INTO Products (name, price, quantity) VALUES (?, ?, ?)''', product)
            cursor.connection.commit()


def select_all_data_from_table():
    add_data_to_products_table()
    with DBManager("shop.db") as cursor:
        res = cursor.execute('''SELECT * FROM Products''')
        print(res.fetchall())
        cursor.connection.commit()


def select_products_by_price():
    add_data_to_products_table()
    with DBManager("shop.db") as cursor:
        res = cursor.execute('''SELECT * FROM Products WHERE price > 0.25''')
        print(res.fetchall())
        cursor.connection.commit()


def update_banana_price():
    add_data_to_products_table()
    with DBManager("shop.db") as cursor:
        cursor.execute('''UPDATE Products SET price = 0.25 WHERE name = "Banana"''')
        cursor.connection.commit()


def delete_apple_from_table():
    add_data_to_products_table()
    with DBManager("shop.db") as cursor:
        cursor.execute('''DELETE FROM Products WHERE name = "Apple"''')
        cursor.connection.commit()
