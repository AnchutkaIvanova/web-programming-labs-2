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
            <ol>
               <a href="/lab1" target="_blank" >Первая лабораторная</a>
             </ol>
            &copy; Иванова Анна Алексеевна, ФБИ-14, 3 курс, 2023
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
     <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css') + '''">
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