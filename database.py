import sqlite3


# Подключение к БД
connection = sqlite3.connect('shop.db', check_same_thread=False)
# Связь между Python и SQL
sql = connection.cursor()


# Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users ('
            'id INTEGER, '
            'name TEXT, '
            'number TEXT, '
            'location TEXT'
            ');')
# Создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products ('
            'pr_id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'pr_name TEXT, '
            'pr_count INTEGER, '
            'pr_description TEXT, '
            'pr_price REAL, '
            'pr_photo TEXT'
            ');')
# Создание таблицы корзины
sql.execute('CREATE TABLE IF NOT EXISTS cart ('
            'id INTEGER, '
            'user_pr_name TEXT, '
            'user_pr_count INTEGER'
            ');')


## Методы для пользователя ##
# Проверка на наличие юзера в БД
def check_user(id):
    check = sql.execute('SELECT * FROM users WHERE id=?;', (id,))
    if check.fetchone():
        return True
    else:
        return False


# Регистрация пользователя
def register(id, name, number, location):
    sql.execute('INSERT INTO users VALUES(?, ?, ?, ?);', (id, name, number, location))
    # Фиксируем изменения
    connection.commit()

