import sqlite3

def create_database():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Создание таблицы countries
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
    ''')

    # Вставка записей в таблицу countries
    countries = [('Франция',), ('Испания',), ('Италия',)]
    cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)

    # Создание таблицы cities
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    )
    ''')

    # Вставка записей в таблицу cities
    cities = [
        ('Париж', 105.4, 1),
        ('Марсель', 240.6, 1),
        ('Мадрид', 604.3, 2),
        ('Барселона', 101.9, 2),
        ('Рим', 1285.3, 3),
        ('Милан', 181.8, 3),
        ('Неаполь', 119.0, 3)
    ]
    cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)

    # Создание таблицы students
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities (id)
    )
    ''')

    # Вставка записей в таблицу students
    students = [
        ('Роберт', 'Дауни', 1),
        ('Крис', 'Эванс', 1),
        ('Скарлетт', 'Йоханссон', 2),
        ('Марк', 'Руффало', 2),
        ('Крис', 'Хемсворт', 3),
        ('Джереми', 'Реннер', 3),
        ('Пол', 'Радд', 4),
        ('Бенедикт', 'Камбербэтч', 4),
        ('Том', 'Холланд', 5),
        ('Чедвик', 'Боузман', 5),
        ('Бри', 'Ларсон', 6),
        ('Сэмюэл', 'Л. Джексон', 6),
        ('Элизабет', 'Олсен', 7),
        ('Крис', 'Пратт', 7),
        ('Зои', 'Салдана', 7)
    ]
    cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students)

    conn.commit()
    conn.close()

def display_students(city_id):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))

    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город проживания: {student[3]}, Площадь города: {student[4]}")
    else:
        print("Нет учеников в выбранном городе.")

    conn.close()

def main():
    create_database()

    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    for city in cities:
        print(f"{city[0]}: {city[1]}")

    while True:
        try:
            city_id = int(input("\nВведите id города: "))
            if city_id == 0:
                break
            display_students(city_id)
        except ValueError:
            print("Пожалуйста, введите допустимый id города.")

if __name__ == '__main__':
    main()
