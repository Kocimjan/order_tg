import sqlite3

def create_tables():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )
    ''')
    
    # Создание таблицы заказов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        bot_name TEXT,
        description TEXT,
        deadline TEXT,
        budget REAL,
        status TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
