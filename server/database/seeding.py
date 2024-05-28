import pandas as pd
import mysql.connector as connector
from connector import get_conn
import base64

def questions():
    path_to_excel_file = "ATHDH.xlsx"
    df = pd.read_excel(path_to_excel_file)
    conn = get_conn()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("delete from questions where 1=1")
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
            conn.rollback()  # Hoàn tác thay đổi nếu có lỗi
            cursor.close()
            conn.close()

    for index, row in df.iterrows():
        print(row[row[5]])
        correct_answer = row[row[5]].replace('\'','\"')
        question_name = row[0].replace('\'','\"')
        conn = get_conn()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("insert into questions (question_name, correct_answer) values(%s, %s)",(question_name,correct_answer))
                conn.commit()
                cursor.close()
                conn.close()
            except Exception as e:
                print(e)
                conn.rollback()
                cursor.close()
                conn.close()
                
def users():
    conn = get_conn()
    username = 'ngn'
    password = base64.b64encode(b'ngn@ngn')
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("insert into users (username, password) values(%s, %s)",(username,password))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
            conn.rollback()
            cursor.close()
            conn.close()
    
questions()