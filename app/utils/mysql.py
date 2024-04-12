import pprint
import pymysql.cursors

class Mysql():
    def __init__(self, **config):
        self.database = 'test_db'
        self.connection = pymysql.connect(
            **config
        )
        self.init()

    def init(self):
        with self.connection.cursor() as cursor:
            exist = cursor.execute(f'SHOW DATABASES LIKE "{self.database}"')
            if not exist:
                cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
                with open('app/utils/schema.sql', 'r', encoding='utf8') as f:
                    cursor.execute(f'USE {self.database}')
                    content = f.readlines()
                    sql = ['']
                    for line in content:
                        if line == '\n':
                            sql.append('')
                        else:
                            sql[-1] += line
                    for s in sql:
                        cursor.execute(s)
            else:
                # cursor.execute(f'DROP database {self.database};')
                # self.init()
                self.connection.select_db(self.database)

    def fetch_one(self, sql: str, args: tuple):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, tuple(args))
                result = cursor.fetchone()
            return result
        except Exception as e:
            print(e.with_traceback())
            return str(e)


    def insert_one(self, sql: str, args: tuple):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, args)
                self.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(e.with_traceback())
            return str(e)



mysql = Mysql(
    host='localhost',
    user='root',
    password='root',
    cursorclass=pymysql.cursors.DictCursor
)
