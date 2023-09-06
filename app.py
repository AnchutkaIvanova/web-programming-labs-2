from flask import Flask 
app = Flask(__name__)

@app.route( "/")
def start():
    return """
    <!doctype html>
    <html>
       <head>
           <title>Иванова Анна, лабораторная 1 </title>
    </head>   
    <body>
        <header>
            НГТУ, ФБ, Лабораторнеая работа 1
        </header>
    
        <h1>web-сервер на flaks</h1>

        <footer>
            &copy; Анна Иванова, Фби-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""
