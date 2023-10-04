from flask import Flask, redirect, url_for,render_template
#url_for возвращает нужный нам путь в виде строки.
#redirect - автоматическая переадресация посетителя с одного URL-адреса на другой.
#из пакета flask добываем класс Flask:
app = Flask(__name__) #Объект приложения 
@app.route("/")#Первый роут, или путь
@app.route("/index")
def start():
    return redirect("/menu", code=302)# Return возвращает значение функции, возвращать означает выдать результат вычисления функции. 

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
                <a href="/menu" target="_blank" >Меню</a>          # CСылка, прикоротой меню открывается в новом окне
                
                <h2>Реализованные роуты</h2>
                <ul>
                   <li>
                      <a href="/lab1/oak" target="_blank" >/lab1/oak - дуб</a>
                   </li>
                   <li>
                      <a href="/lab1/student" target="_blank" >/lab1/student - студент</a>
                   </li>
                   <li>
                      <a href="/lab1/python" target="_blank" >/lab1/python - python</a>
                   </li>
                   <li>
                      <a href="/lab1/karakal" target="_blank" >/lab1/karakal - каракал</a>
                   </li>
                </ul>

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
     <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">  #фрейворк указывает путь к файлу, link, нужен для подключения стилей
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
@app.route('/lab1/student')
def student():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Иванова Анна Алексеевна, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <h1>Иванова Анна</h1>
          <img src=''' + url_for('static', filename='logo.jpg') + '''>
    <footer>
    &copy; Иванова Анна, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Иванова Анна Алексеевна, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <p>Python – это универсальный современный ЯП высокого уровня, к преимуществам которого относят высокую
           производительность программных решений и структурированный, хорошо читаемый код.  Синтаксис Питона 
           максимально облегчен, что позволяет выучить его за сравнительно короткое время. Ядро имеет очень
           удобную структуру, а широкий перечень встроенных библиотек позволяет применять внушительный набор
           полезных функций и возможностей. ЯП может использоваться для написания прикладных приложений, 
           а также разработки WEB-сервисов.</p>
          
          <p>Python может поддерживать широкий перечень стилей разработки приложений,
           в том числе, очень удобен для работы с ООП и функционального программирования.</p>
          
          <p>Питон – не самый «молодой» язык программирования, но и не слишком старый. К моменту его создания уже
           существовали такие «монстры», как Паскаль или Си. А потому при создании ЯП авторы старались взять лучшее
           из различных платформ для разработчиков. Фактически Python представляет из себя своеобразный «джем» 
           удачных решений более чем из 8 различных языков. К примеру, байт компиляция появилась еще до создания
           Питона, но была очень удачна в него интегрирована.</p>

          <img src=''' + url_for('static', filename='python.jpg') + '''>
    <footer>
    &copy; Иванова Анна, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''
@app.route('/lab1/karakal')
def karakal():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Иванова Анна Алексеевна, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <p>Каракал – это не что иное, как дикая кошка, обладающая обтекаемым, стройным телом, покрытая короткой 
          шерстью золотисто-красноватого оттенка, а также с уникальным рисунком в области морды. Каракала 
          по-другому еще называют пустынной рысью, хотя рысь отличается более короткими конечностями, а также 
          присутствием на шерстяном покрове своеобразного рисунка, в виде полос и пятен.</p>
          
          <p>Это самые быстрые, а также и самые крупные дикие кошки Африканского континента.
           Прежде, чем современные каракалы обрели тот вид и то анатомическое строение тела, 
           прошло около 4-х десятков миллионов лет.</p>
          
          <p>Несмотря на то, что каракалы практически исчезли на севере Африки, на ее других территориях
           еще достаточно много этих животных. Перспективными территориями расселения подобных животных 
           считается пустыня Сахара, а также экваториальный пояс зеленых насаждений Западной и Центральной Африки.
           На юге Африки, а также в Намибии каракалов настолько много, что их истребляют как вредное животное. 
           На территории Азии обитают не столь многочисленные популяции.</p>

          <img src=''' + url_for('static', filename='kar.jpg') + '''>
    <footer>
    &copy; Иванова Анна, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Иванова Анна'
    return render_template('example.html', name=name)