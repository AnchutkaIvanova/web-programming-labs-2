from flask import Flask, redirect, url_for
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
            <h1>web-сервер на flask</h1>
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
           <title>Иванова Анна Алексеевна, лабораторная 6</title>
	
            </header>
            <h1>web-сервер на flask</h1>
            <menu>Первая лабораторная</menu>
            <p>
            Flask - фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </p>
            <footer>
            &copy; Анна Алексеевна, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""
