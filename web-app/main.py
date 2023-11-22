"""This module contains the Flask application."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a 'Hello, World!' string."""
    return 'Hello, World!'

