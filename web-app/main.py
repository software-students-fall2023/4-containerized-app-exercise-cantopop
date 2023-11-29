"""This module contains the Flask application."""

from flask import Flask, render_template, request, redirect, url_for
from camera_capture import capture_image, save_image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/capture")
def capture():
    """Capture an image and display it on the web page."""
    try:
        frame = capture_image()
        save_image(frame, "static/captured.jpg")
        return render_template("capture.html", image_path="static/captured.jpg")
    except Exception as e:  # pylint: disable=broad-except
        return str(e)


@app.route('/take-photo', methods=['POST'])
def take_photo():
    frame = capture_image()
    if frame is not None:
        image_path = os.path.join('static', 'captured_image.jpg')
        save_image(frame, image_path)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
