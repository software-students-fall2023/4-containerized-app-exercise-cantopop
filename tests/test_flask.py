import pytest
from web-app import app as flask_app  # Import your Flask app
import mongomock
from pymongo.mongo_client import MongoClient

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a new app instance for testing
    app = flask_app
    app.config['TESTING'] = True

    # Use mongomock to mock the MongoDB
    app.config['db'] = mongomock.MongoClient().db

    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_show_main_screen(client):
    """Test the main screen route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'main_screen.html' in response.data

def test_show_add_notes(client):
    """Test the add notes screen route."""
    response = client.get('/add')
    assert response.status_code == 200
    assert b'add_notes.html' in response.data

def test_add_notes(client, app):
    """Test adding notes."""
    # Mock data for posting a note
    mock_note = {'title': 'Test Title', 'main_body': 'Test Body'}
    response = client.post('/add', data=mock_note, follow_redirects=True)
    assert response.status_code == 200
    assert b'Added Successfully' in response.data

    # Verify the note is added in the mocked database
    with app.app_context():
        db = app.config['db']
        assert db.notes.find_one({'title': 'Test Title'})
