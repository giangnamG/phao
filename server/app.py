from flask import Flask, render_template, request, session
from database.connector import get_conn
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ngn@ngn'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html',username=session.get('username'),keyword='keyword', results=None) 
    elif request.method == 'POST':
        if session.get('username') != None:
            keyword = request.form.get('keyword')
            conn = get_conn()
            results = None
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute('select * from questions where question_name like %s',('%'+keyword+'%',))
                    results = cursor.fetchall()
                    conn.commit()
                    cursor.close()
                    conn.close()
                except Exception as e:
                    print(e)
                    conn.rollback()  # Hoàn tác thay đổi nếu có lỗi
                    cursor.close()
                    conn.close()
            if results == None:
                return render_template('index.html',username=session.get('username'),results=None, keyword=keyword,res_message="Nhập lại keyword")
            else:
                return render_template('index.html',username=session.get('username'),results=results, keyword=keyword,res_message="Nhập lại keyword") 
        else:
            return render_template('index.html',username=session.get('username'),results=None, keyword='keyword',message='you need to login') 
            
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = base64.b64encode(request.form.get('password').encode('utf-8'))
    conn = get_conn()
    user = None
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("select * from users where username=%s and password = %s", (username, password))
            user = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
            conn.rollback()  # Hoàn tác thay đổi nếu có lỗi
            cursor.close()
            conn.close()
    message = None
    if len(user) > 0:
        message = 'login successful'
        session['username'] = username
    else:
        message = 'login failed'
    return render_template('index.html',username=session.get('username'),results=None, keyword='keyword',message=message) 
    
@app.route('/logout', methods=['GET'])
def logout():
    session['username'] = None
    return render_template('index.html',username=None,keyword='keyword', results=None) 
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')