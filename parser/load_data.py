import psycopg2

from config import dsn, TIME
from decorators import sleep
from postgres_loader import PostgresLoader


@sleep(TIME)
def save_data_to_db():
    with psycopg2.connect(**dsn) as conn:
        cursor = conn.cursor()
        postgres = PostgresLoader(cursor)
        postgres.parsing_data()
        conn.commit()


if __name__ == "__main__":
    while True:
        save_data_to_db()
