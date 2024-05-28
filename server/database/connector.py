import mysql.connector as connector

# host = 'db'
# user = 'ngn'
# password = 'ngn@ngn'
# database = 'phao_lsd'
host = 'db'
user = 'ngn'
password = 'ngn@ngn'
database = 'phao_lsd'

def get_conn():
    try:
        conn = connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            # charset='utf8mb4',
            # collation = 'utf8mb4_unicode_ci'
        )
        return conn
    except connector.Error as err:
        print("Lỗi: {}".format(err))
        return None
conn = get_conn()