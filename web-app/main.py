"""This module contains the Flask application."""

from flask import Flask, render_template
from camera_capture import capture_image, save_image

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a 'Hello, World!' string."""
    return "Hello, World!"

@app.route('/capture')
def capture():
    try:
        frame = capture_image()
        save_image(frame, 'static/captured.jpg')
        return render_template('capture.html', image_path='static/captured.jpg')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)