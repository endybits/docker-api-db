import os
import pymysql
from pymysql.cursors import DictCursor
from pymysql.err import OperationalError

def db_connection():
    try:
        conn = pymysql.connect(
            host=os.environ.get('HOST_DB','localhost'),
            user='root',
            password=os.environ.get('PASSWORD_DB','DEFAULT_PASS'),
            cursorclass=DictCursor
        )

        return "DB connection successful 💫"
    except OperationalError as e:
        print(f'DB Error: {e}')
        return "Boom 💣💥! DB connection failed"