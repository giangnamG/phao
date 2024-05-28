from connector import get_conn

def questions_table():
    conn = get_conn()
    query = """create table if not exists questions(
                id integer primary key auto_increment, 
                question_name varchar(2000) not null,
                correct_answer varchar(2000) not null)
                """
    if conn:
        try: 
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as err:
            print("Lỗi truy vấn: {} -> {}".format(query, err))
            conn.rollback()  # Hoàn tác thay đổi nếu có lỗi
            cursor.close()
            conn.close()
def users_table():
    conn = get_conn()
    query = """create table if not exists users(
                id integer primary key auto_increment, 
                username varchar(50) not null unique,
                password varchar(50) not null)
                """
    if conn:
        try: 
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as err:
            print("Lỗi truy vấn: {} -> {}".format(query, err))
            conn.rollback()  # Hoàn tác thay đổi nếu có lỗi
            cursor.close()
            conn.close()