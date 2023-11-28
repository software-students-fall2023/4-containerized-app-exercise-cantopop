from flask import Flask, render_template, request, redirect, url_for
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

app = Flask(__name__)
#uri = os.getenv('MONGODB_URI')
uri = "mongodb+srv://admin:admin123@cluster0.m5t5gvu.mongodb.net/?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
connection = MongoClient(uri, server_api=ServerApi('1'))
db = connection["note_app"]
notes = db.notes

@app.route('/')
def show_main_screen():
   return render_template('main_screen.html')

@app.route('/add')
def show_add_notes():
    return render_template('add_notes.html', message = "")

@app.route('/add', methods=['POST'])
def add_notes():
    title = request.form['title']
    main_body = request.form['main_body']

    dup = 0
    static_title = title
    while(notes.count_documents({"title": title})):
        dup += 1
        title = static_title + "_" + str(dup)

    doc = {
        "title" : title,
        "main_body" : main_body,
        }
    notes.insert_one(doc)
    return render_template('add_notes.html', message = "Added Successfully")

@app.route('/show_edit_note')
def show_edit_note():
    title = request.args.get('title')
    doc = notes.find_one({"title": title})
    main_body = doc["main_body"]
    return render_template("edit_note.html", title = title, main_body = main_body)

@app.route('/edit_confirm/<title>', methods=['POST'])
def edit_note_confirm(title):
    new_title = request.form['title']
    dup = 0
    static_title = new_title
    while(notes.count_documents({"title": new_title}) and new_title != title):
         dup += 1
         new_title = static_title + "_" + str(dup)
         print(new_title)
    new_main_body = request.form['main_body']
    update = {}
    update["title"] = new_title
    update["main_body"] = new_main_body
    notes.update_one({'title': title}, {"$set": update})
    return render_template('edit_note.html', title = new_title, main_body = new_main_body, message = "Note Updated")

@app.route('/delete_note/<title>')
def delete_note(title):
    notes.delete_one({"title": title})
    return redirect(url_for("show_all_notes"))

@app.route('/show_all_notes')
def show_all_notes():
    docs = notes.find({}).sort('title', 1)
    if len(list(notes.find({}))) == 0:
        return render_template('show_all_notes.html')    
    return render_template('show_all_notes.html', docs = docs)

@app.route('/show_search_notes')
def show_search_notes():
    return render_template("search_notes.html", docs = {}, message ="")

@app.route('/search', methods=['POST'])
def search_notes():
    keywords = request.form['keywords']
    docs = notes.find({}).sort("title", 1)
    found = []
    for doc in docs:
        if doc["title"].count(keywords):
            found.append(doc)
    if found == []:
        return render_template("search_notes.html", message ="Notes Not Found")
    return render_template("search_notes.html", docs = found, message ="")


    