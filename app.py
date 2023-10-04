from flask import Flask, redirect, url_for
#url_for возвращает нужный нам путь в виде строки.
app = Flask(__name__)
@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return"""
<!doctype html>
<html>
     <head>
           <title>НГТУ, ФБ, Лабораторные работы</title>
     </head>
     <body>
            <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Спиок лабораторных
            </header>

            <ol>
             <a href="/lab1" target="_blank" >Первая лабораторная</a>
            </ol>

            <footer>
            &copy; Иванова Анна Алексеевна, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
     <head>
           <title>Иванова Анна Алексеевна, лабораторная 1</title>
     </head>
     <body>
            <header>
            НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>web-сервер на flask</h1>
              <menu>Первая лабораторная</menu>
            <p>
            Flask - фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </p>
                <a href="/menu"target="_blank>Меню</a>

            <footer>
            &copy; Анна Алексеевна, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return'''
<!doctype html>
<html>
     <head>
        <title>Иванова Анна Алексеевна, лабораторная 1</title>
    </head>
     <body>
     <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <h1>Дуб</h1>
          <img src=''' + url_for('static', filename='oak.jpg') + '''>
    <footer>
    &copy; Иванова Анна, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
