# import os

import psycopg2
# from dotenv import load_dotenv
from env_test import DBNAME, USER, PASSWORD, PORT, HOST

# вопрос к наставнику - как это настроить
# load_dotenv()
# DBNAME = os.getenv("DBNAME")
# USER = os.getenv("USER")
# PASSWORD = os.getenv("PASSWORD")
# PORT = os.getenv("PORT")
# HOST = os.getenv("HOST")

# Создайте подключение к базе данных
conn = psycopg2.connect(
    dbname=DBNAME,
    user=USER,
    password=PASSWORD,
    port=PORT,
    host=HOST
)

# Открытие курсора
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS test_table")
cur.execute("CREATE TABLE test_table (id int PRIMARY KEY, name varchar(100) NOT NULL)")
conn.commit()

cur.execute("INSERT INTO test_table (id, name) values (1, 'Kirill')")


# коммит
conn.commit()

cur.execute()

#закрыть курсор и соединение
cur.close()
conn.close()