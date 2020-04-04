from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    notes_file = open("notes.txt", "r", encoding = "UTF-8")
    notes_list = [row for row in notes_file]
    notes_file.close()
    return render_template('index.html', notes_list = notes_list)



@app.route("/hello/<string:name>")
def hello(name):
    name = name.capitalize()
    return render_template("hello.html", name = name)



@app.route("/add")
def add():
    return render_template("add.html")



@app.route("/add-note", methods = ["POST"])
def add_note():
    note = request.form.get("note")
    notes_file = open('notes.txt', 'a+', encoding = "UTF-8")
    notes_file.write(str(note) + "\n")
    notes_file.close()
    return render_template("qwerty.html")