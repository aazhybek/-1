import sqlite3

# Создание базы данных и таблицы
def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()

# Функция для добавления 15 различных товаров
def add_products():
    products = [
        ('Product 1', 19.99, 10),
        ('Product 2', 29.99, 5),
        ('Product 3', 9.99, 15),
        ('Product 4', 49.99, 7),
        ('Product 5', 99.99, 3),
        ('Product 6', 5.99, 20),
        ('Product 7', 15.99, 8),
        ('Product 8', 25.99, 6),
        ('Product 9', 35.99, 4),
        ('Product 10', 45.99, 12),
        ('Product 11', 55.99, 9),
        ('Product 12', 65.99, 11),
        ('Product 13', 75.99, 2),
        ('Product 14', 85.99, 14),
        ('Product 15', 95.99, 1)
    ]

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()

# Функция для изменения количества товара по ID
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, product_id))

    conn.commit()
    conn.close()

# Функция для изменения цены товара по ID
def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, product_id))

    conn.commit()
    conn.close()

# Функция для удаления товара по ID
def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (product_id,))

    conn.commit()
    conn.close()

# Функция для выборки всех товаров
def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

# Функция для выборки товаров по условию цены и количества
def get_products_by_price_and_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

# Функция для поиска товаров по названию
def search_products_by_title(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

# Тестирование функций
def test_functions():
    # Создание базы данных и таблицы
    create_database()

    # Добавление продуктов
    add_products()

    # Обновление количества товара
    update_quantity(2, 25)

    # Обновление цены товара
    update_price(3, 35.99)

    # Удаление товара
    delete_product(4)

    # Получение всех товаров
    print("Все товары:")
    get_all_products()

    # Получение товаров по условию цены и количества
    print("\nТовары дешевле 100 сомов и количеством больше 5 шт:")
    get_products_by_price_and_quantity(100, 5)

    # Поиск товаров по названию
    print("\nПоиск товаров с названием 'Product':")
    search_products_by_title('Product')

# Запуск тестирования
if __name__ == "__main__":
    test_functions()
