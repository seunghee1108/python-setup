from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MariaDB 연결 설정
db = mysql.connector.connect(
    host="localhost",        # MariaDB 호스트
    user="root",             # 사용자 이름
    password="1108",         # 암호
    database="flask"         # 데이터베이스 이름
)

# 마리아디비 커서 생성
cursor = db.cursor()

# 회원가입 폼을 위한 라우트 및 로직
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 이메일 등 다른 필드도 여기에 추가할 수 있습니다.

        # 회원가입 정보를 데이터베이스에 저장하는 쿼리 실행
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()  # 데이터베이스에 변경 사항을 반영하기 위해 commit()

        # 회원가입 후 로그인 페이지로 리다이렉트
        return redirect(url_for('login'))

    return render_template('register.html')  # 회원가입 폼을 렌더링

# 로그인 폼을 위한 라우트 및 로직
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 로그인 정보 확인을 위한 쿼리 실행
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchall()

        if result:
            return "로그인 성공"  # 로그인 성공 시 어떤 동작을 수행할지 여기에 추가할 수 있습니다.
        else:
            return "로그인 실패"  # 로그인 실패 시 어떤 동작을 수행할지 여기에 추가할 수 있습니다.

    return render_template('index.html')  # 로그인 폼을 렌더링

# 인덱스 페이지를 위한 라우트
@app.route('/')
def index():
    return render_template('index.html')  # 인덱스 페이지를 렌더링

if __name__ == '__main__':
    app.run(debug=True)
