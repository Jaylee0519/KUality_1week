from flask import Flask, render_template, redirect

app = Flask(__name__)

# 메인 페이지 (자기소개)
@app.route("/")
def index():
    return render_template('index.html')

# 학과 시간표 페이지
@app.route("/schedule/")
def schedule():
    return render_template('schedule.html')

# 게시판 페이지
@app.route("/board/")
def board():
    return render_template('board.html')

# 로그인 페이지
@app.route("/login/")
def login():
    return render_template('login.html')

# 회원가입 페이지
@app.route("/sign_up/")
def sign_up():
    return render_template('sign_up.html')

if __name__ == "__main__":
    app.run(debug=True)
