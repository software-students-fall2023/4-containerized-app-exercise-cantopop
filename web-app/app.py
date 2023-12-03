"""
base64: provides function that can convert image into mongodb compatible format
flask: web-app frame work
pymongo: provide connection to the mongodb
os: retreiving env var
"""
# import os
import base64
from flask import Flask, render_template, request, redirect, url_for
from pymongo.mongo_client import MongoClient

app = Flask(__name__)
# URI = os.getenv("MONGODB_URI")
URI = "mongodb+srv://admin:admin123@cluster0.m5t5gvu.mongodb.net/?retryWrites=true&w=majority"
app.config["MONGO_URI"] = URI
connection = MongoClient(app.config["MONGO_URI"])
db = connection["note_app"]
notes = db.notes
temp = db.temp


@app.route("/")
def show_main_screen():
    """
    Show the home page of the application
    """
    return render_template("main_screen.html")


@app.route("/capture_image")
def capture_image():
    """
    Invoke the webcam to caputre images
    """
    return render_template("camera.html")


@app.route("/upload_image", methods=["POST"])
def upload_image():
    """
    Invoked by pressing the captured button by camera.html, upload encoded image to mongodb
    """
    data = request.get_json()
    if data and "imageData" in data:
        image_data = data["imageData"]
        _, encoded = image_data.split(",", 1)
        binary_data = base64.b64decode(encoded)

        doc = {
            "title": "",
            "main_body": "",
            "processed": False,
            "raw_image": binary_data,
        }
        temp.insert_one(doc)
    return render_template("buffer.html")


@app.route("/add")
def show_add_notes():
    """
    Show the mlc processed title and main body; if processing not done, then busy waiting
    """
    while temp.find_one({"processed": True}) is None:
        pass
    doc = temp.find_one_and_delete({})
    temp.delete_many({})
    return render_template(
        "add_notes.html", title=doc["title"], main_body=doc["main_body"]
    )


@app.route("/add", methods=["POST"])
def add_notes():
    """
    Add note to mongodb
    """
    title = request.form["title"]
    main_body = request.form["main_body"]

    dup = 0
    static_title = title
    while notes.count_documents({"title": title}):
        dup += 1
        title = static_title + "_" + str(dup)

    doc = {
        "title": title,
        "main_body": main_body,
    }
    notes.insert_one(doc)
    return render_template("add_notes.html", message="Added Successfully")


@app.route("/show_edit_note")
def show_edit_note():
    """
    Find the note that needs to be edit, and show the editing interface
    """
    title = request.args.get("title")
    doc = notes.find_one({"title": title})
    main_body = doc["main_body"]
    return render_template("edit_note.html", title=title, main_body=main_body)


@app.route("/edit_confirm/<title>", methods=["POST"])
def edit_note_confirm(title):
    """
    Update the edited notes in mongodb
    @param title := the original title
    """
    new_title = request.form["title"]
    dup = 0
    static_title = new_title
    while notes.count_documents({"title": new_title}) and new_title != title:
        dup += 1
        new_title = static_title + "_" + str(dup)
        print(new_title)
    new_main_body = request.form["main_body"]
    update = {}
    update["title"] = new_title
    update["main_body"] = new_main_body
    notes.update_one({"title": title}, {"$set": update})
    return render_template(
        "edit_note.html",
        title=new_title,
        main_body=new_main_body,
        message="Note Updated",
    )


@app.route("/delete_note/<title>")
def delete_note(title):
    """
    Delete the selected note from mongodb
    """
    notes.delete_one({"title": title})
    return redirect(url_for("show_all_notes"))


@app.route("/show_all_notes")
def show_all_notes():
    """
    Retrived all notes from mongodb
    """
    docs = notes.find({}).sort("title", 1)
    if len(list(notes.find({}))) == 0:
        return render_template("show_all_notes.html")
    return render_template("show_all_notes.html", docs=docs)


@app.route("/show_search_notes")
def show_search_notes():
    """
    Show the search page
    """
    return render_template("search_notes.html", docs={}, message="")


@app.route("/search", methods=["POST"])
def search_notes():
    """
    Show all the notes that match with the keywords provided
    """
    keywords = request.form["keywords"]
    docs = notes.find({}).sort("title", 1)
    found = []
    for doc in docs:
        if doc["title"].count(keywords):
            found.append(doc)
    if not found:
        return render_template("search_notes.html", message="Notes Not Found")
    return render_template("search_notes.html", docs=found, message="")
