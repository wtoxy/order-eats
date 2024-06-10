from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from model import *
import psycopg2

# Указываем параметры подключения к базе данных PostgreSQL
DB_HOST = '104.236.64.26'
DB_NAME = 'ordereats'
DB_USER = 'ordereats'
DB_PASSWORD = 'fatEk(3obE'

# Создаем экземпляр Flask-приложения
app = Flask(__name__)

# Устанавливаем конфигурацию для SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy(app)

conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/restaurant1')
def restaurant1():
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Выполняем SQL-запрос для получения информации о всех блюдах из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat, eat_engl FROM restaurant1"
    cursor.execute(query)
    eats_info = cursor.fetchall()  # Получаем результат запроса

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

    # Передаем информацию о блюдах в шаблон restaurant1.html для отображения
    return render_template('restaurant1.html', eats=eats_info)


@app.route('/restaurant1_cheesecake')
def restaurant1_cheesecake():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant1 WHERE name_of_eat = 'Чизкейк Нью-Йорк'"
    cursor.execute(query)
    cheesecake = cursor.fetchone()
    if cheesecake:
        food_name = cheesecake[0]
        cost_of_eat = cheesecake[1]
    else:
        food_name = "Чизкейк Нью-Йорк"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return render_template('order_eat.html', food_name=food_name, cost_of_eat=cost_of_eat)


@app.route('/restaurant1_triumph')
def restaurant1_triumph():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant1 WHERE name_of_eat = 'Триумф'"
    cursor.execute(query)
    triumph = cursor.fetchone()
    if triumph:
        food_name = triumph[0]
        cost_of_eat = triumph[1]
    else:
        food_name = "Триумф"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant1_bananas')
def restaurant1_bananas():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant1 WHERE name_of_eat = 'Творожно-банановый десерт'"
    cursor.execute(query)
    bananas = cursor.fetchone()
    if bananas:
        food_name = bananas[0]
        cost_of_eat = bananas[1]
    else:
        food_name = "Творожно-банановый десерт"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant1_donuts')
def restaurant1_donuts():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant1 WHERE name_of_eat = 'Пончики'"
    cursor.execute(query)
    donuts = cursor.fetchone()
    if donuts:
        food_name = donuts[0]
        cost_of_eat = donuts[1]
    else:
        food_name = "Пончики"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant2')
def restaurant2():
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Выполняем SQL-запрос для получения информации о всех блюдах из таблицы restaurant2
    query = "SELECT name_of_eat, cost_of_eat, eat_engl FROM restaurant2"
    cursor.execute(query)
    eats_info = cursor.fetchall()  # Получаем результат запроса

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

    # Передаем информацию о блюдах в шаблон restaurant2.html для отображения
    return render_template('restaurant2.html', eats=eats_info)


@app.route('/restaurant2_peperoni')
def restaurant2_peperoni():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant2
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant2 WHERE name_of_eat = 'Пеперони'"
    cursor.execute(query)
    peperoni = cursor.fetchone()
    if peperoni:
        food_name = peperoni[0]
        cost_of_eat = peperoni[1]
    else:
        food_name = "Пеперони"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant2_margarita')
def restaurant2_margarita():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant2
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant2 WHERE name_of_eat = 'Маргарита'"
    cursor.execute(query)
    margarita = cursor.fetchone()
    if margarita:
        food_name = margarita[0]
        cost_of_eat = margarita[1]
    else:
        food_name = "Маргарита"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant2_moreprodukty')
def restaurant2_moreprodukty():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant2
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant2 WHERE name_of_eat = 'Пицца с морепродуктами'"
    cursor.execute(query)
    moreprodukty = cursor.fetchone()
    if moreprodukty:
        food_name = moreprodukty[0]
        cost_of_eat = moreprodukty[1]
    else:
        food_name = "Пицца с морепродуктами"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant2_icecream')
def restaurant2_icecream():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant2
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant2 WHERE name_of_eat = 'Пицца с мороженым'"
    cursor.execute(query)
    icecream = cursor.fetchone()
    if icecream:
        food_name = icecream[0]
        cost_of_eat = icecream[1]
    else:
        food_name = "Пицца с мороженым"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant3')
def restaurant3():
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Выполняем SQL-запрос для получения информации о всех блюдах из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat, eat_engl FROM restaurant3"
    cursor.execute(query)
    eats_info = cursor.fetchall()  # Получаем результат запроса

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

    # Передаем информацию о блюдах в шаблон restaurant3.html для отображения
    return render_template('restaurant3.html', eats=eats_info)


@app.route('/restaurant3_pahlava')
def restaurant3_pahlava():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant3
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant3 WHERE name_of_eat = 'Пахлава'"
    cursor.execute(query)
    pahlava = cursor.fetchone()
    if pahlava:
        food_name = pahlava[0]
        cost_of_eat = pahlava[1]
    else:
        food_name = "Пахлава"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant3_bozbash')
def restaurant3_bozbash():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant3
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant3 WHERE name_of_eat = 'Бозбаш'"
    cursor.execute(query)
    bozbash = cursor.fetchone()
    if bozbash:
        food_name = bozbash[0]
        cost_of_eat = bozbash[1]
    else:
        food_name = "Бозбаш"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant3_lyulya')
def restaurant3_lyulya():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant3
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant3 WHERE name_of_eat = 'Люля кебаб'"
    cursor.execute(query)
    lyulya = cursor.fetchone()
    if lyulya:
        food_name = lyulya[0]
        cost_of_eat = lyulya[1]
    else:
        food_name = "Люля кебаб"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant3_pig')
def restaurant3_pig():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant3
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant3 WHERE name_of_eat = 'Шашлык из свинины'"
    cursor.execute(query)
    pig = cursor.fetchone()
    if pig:
        food_name = pig[0]
        cost_of_eat = pig[1]
    else:
        food_name = "Шашлык из свинины"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant4')
def restaurant4():
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Выполняем SQL-запрос для получения информации о всех блюдах из таблицы restaurant1
    query = "SELECT name_of_eat, cost_of_eat, eat_engl FROM restaurant4"
    cursor.execute(query)
    eats_info = cursor.fetchall()  # Получаем результат запроса

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

    # Передаем информацию о блюдах в шаблон restaurant4.html для отображения
    return render_template('restaurant4.html', eats=eats_info)


@app.route('/restaurant4_philadelphia')
def restaurant4_philadelphia():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant4
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant4 WHERE name_of_eat = 'Филадельфия'"
    cursor.execute(query)
    philadelphia = cursor.fetchone()
    if philadelphia:
        food_name = philadelphia[0]
        cost_of_eat = philadelphia[1]
    else:
        food_name = "Филадельфия"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant4_california')
def restaurant4_california():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant4
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant4 WHERE name_of_eat = 'Калифорния'"
    cursor.execute(query)
    california = cursor.fetchone()
    if california:
        food_name = california[0]
        cost_of_eat = california[1]
    else:
        food_name = "Калифорния"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant4_tuna')
def restaurant4_tuna():
    # Выполняем SQL-запрос для получения названия блюда из таблицы restaurant4
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant4 WHERE name_of_eat = 'Запеченные роллы с тунцом'"
    cursor.execute(query)
    tuna = cursor.fetchone()
    if tuna:
        food_name = tuna[0]
        cost_of_eat = tuna[1]
    else:
        food_name = "Запеченные роллы с тунцом"  # Указываем название блюда по умолчанию
        cost_of_eat = 0
    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/restaurant4_chicken')
def restaurant4_chicken():
    # Выполняем SQL-запрос для получения названия и цены блюда из таблицы restaurant4
    query = "SELECT name_of_eat, cost_of_eat FROM restaurant4 WHERE name_of_eat = 'Запеченные роллы с курицей'"
    cursor.execute(query)
    chicken = cursor.fetchone()
    if chicken:
        food_name = chicken[0]
        cost_of_eat = chicken[1]
    else:
        food_name = "Запеченные роллы с курицей"  # Указываем название блюда по умолчанию
        cost_of_eat = 0  # Указываем цену по умолчанию

    return redirect(url_for('order_eat', food_name=food_name, cost_of_eat=cost_of_eat))


@app.route('/order_eat')
def order_eat():
    food_name = request.args.get('food_name')
    cost_of_eat = request.args.get('cost_of_eat')
    total = request.args.get('total')
    return render_template('order_eat.html', food_name=food_name, cost_of_eat=cost_of_eat, total=total)



