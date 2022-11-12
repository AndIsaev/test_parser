import psycopg2

from postgres_loader import PostgresLoader


dsn = {
    "dbname": 'backend',
    "user": 'postgres',
    "password": 'super',
    "host": 'db',
    "port": 5432
}


def save_data_to_db():
    with psycopg2.connect(**dsn) as conn:
        cursor = conn.cursor()
        postgres = PostgresLoader(cursor)
        postgres.parsing_data()
        conn.commit()


if __name__ == "__main__":
    while True:
        save_data_to_db()
