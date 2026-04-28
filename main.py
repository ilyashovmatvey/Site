from flask import Flask, render_template
import os

app = Flask(__name__)

base_url = "http://127.0.0.1:5000"

@app.route("/")
def start():
    return render_template("start.html", Title = "Главная страница сайта")


@app.route("/index")
def index():
    return render_template("index.html", Title = "Главная страница заданий")

@app.route("/index2")
def index2():
    return render_template("index2.html", Title = "Главная страница правил")




@app.route("/page")
def page():
    return render_template("page.html", Title = "Слова с суфиксом Н и НН")

@app.route("/page2")
def page2():
    return render_template("page2.html", Title = "Правильные ответы на суффиксы")

@app.route("/page3")
def page3():
    return render_template("page3.html", Title = "Правила правописания Н и НН")



@app.route("/contacts")
def contacts():
    return render_template("contacts.html", Title = "Слова с приставкой ПРИ и ПРЕ")

@app.route("/contacts2")
def contacts2():
    return render_template("contacts2.html", Title = "Правильные ответы на приставки")

@app.route("/contacts3")
def contacts3():
    return render_template("contacts3.html", Title = "Правила по правописанию приставки ПРЕ и ПРИ")


@app.route("/confuse")
def confuse():
    return render_template("confuse.html", Title = "Правописание Ы и И")

@app.route("/confuse2")
def confuse2():
    return render_template("confuse2.html", Title = "Правильные ответы на правописание")

@app.route("/confuse3")
def confuse3():
    return render_template("confuse3.html", Title = "Правила про правописанию Ы и И после приставки")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))