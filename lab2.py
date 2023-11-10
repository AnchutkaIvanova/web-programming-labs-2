from flask import Blueprint, redirect, url_for,render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example')
def example():
    name = 'Иванова Анна'
    laba2 = 'Лабораторная работа 2'

    group = 'ФБИ-14'

    kurs = '3 курс'
    student = 'Иванова Анна'


    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
        ]

    books = [
        {'author': 'Толстой Л.Н.', 'nazv': 'Анна Каренина', 'zanr': 'Классика', 'str': '159'},
        {'author': 'Джейн Остин', 'nazv': 'Гордость и предубеждение', 'zanr': 'Классика', 'str': '423'},
        {'author': 'Патрик Ленсиони', 'nazv': 'Евгений Онегин', 'zanr': 'Классика', 'str': '542'},
        {'author': 'Джек Лондон', 'nazv': 'Мартин Иден', 'zanr': 'Классика', 'str': '600'},
        {'author': 'Уильям Шекспир', 'nazv': 'Ромео и джульетта', 'zanr': 'Классика', 'str': '450'},
        {'author': 'Станислав Лем', 'nazv': 'Солярис', 'zanr': 'Фантастика', 'str': '320'},
        {'author': 'Фрэнк Герберт', 'nazv': 'Дюна', 'zanr': 'Фантастика', 'str': '400'},
        {'author': 'Дэн Симмонс', 'nazv': 'Гиперион', 'zanr': 'Фантастика', 'str': '243'},
        {'author': 'Нил Стивенсон', 'nazv': 'Анафем', 'zanr': 'Фантастика', 'str': '156'},
        {'author': 'Айзек Азимов', 'nazv': 'Конец вечности', 'zanr': 'Фантастика', 'str': '356'}
        ]
    return render_template('example.html', 
                            name=name, laba2=laba2, group=group,
                            kurs=kurs, student=student, fruits=fruits, books=books)



@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/cosmetic')
def cosmetic ():
    return render_template('cosmetic.html')


@lab2.route('/777/')
def ziro():
    return 'ziro'