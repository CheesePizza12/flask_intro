from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hi():
    return "Hello World!"


@app.route("/welcome")
def welcome():
    return "how do you doing?"
    
@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요</h1>"

@app.route("/html_line")
def html_line():
    return """
            <h1>여러줄을 보내겠습니다.</h1>
            <ul>
                <li>1번</li>
                <li>2번</li>
            </ul>
            
            """

@app.route("/html_file")
def html_file():
    return render_template("file.html")
    

@app.route("/hello/<string:name>")
def hello(name):
    return render_template("hello.html", people_name=name)

# 사용자가 입력한 숫자를 받아서 세제곱 후 cube.html파일을 통해 응답
# @app.route("/cube/<string:num>")
# def cube(num):
#     num = int(num)
#     num=pow(num,3)
#     return render_template("cube.html", num=num)

@app.route("/cube/<int:num>")
def cube(num):
    result=pow(num,3)
    return render_template("cube.html", result=result, num=num)