from database_connection import get_database_connection


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            password TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE subscriptions (
            user_id TEXT,
            name TEXT,
            price REAL,
            end_date DATE,
            state TEXT,
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT
        );
    ''')



    connection.commit()


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS subscriptions;
    ''')


    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
