#Импорт
from flask import Flask, render_template,request, redirect, request, send_from_directory
import os


app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_db = request.form.get('button_db')
    if button_python:
        return render_template('index2.html', button_python=button_python)
    return render_template('index.html')


@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/discord_ime")
def discord_info():
    return render_template("discord_ime.html")

@app.route("/mnimi1ailiiiaavgo")
def secret1():
    return render_template("mnimi1ailiiiaavgo.html")

@app.route("/hella_best_gnomiks")
def gnomiks():
    return render_template("hella_best_gnomiks.html")

@app.route("/six")
def secret2():
    return render_template("six.html")

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == "__main__":
    app.run(debug=True)
