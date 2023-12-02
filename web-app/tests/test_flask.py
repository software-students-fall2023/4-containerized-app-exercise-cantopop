import pytest
from app import app as flask_app
import mongomock

@pytest.fixture
def create_app():
    """Fixture to create a Flask app for testing."""
    app = flask_app
    app.config['TESTING'] = True
    app.config['db'] = mongomock.MongoClient().db
    return app

@pytest.fixture
def client(create_app):
    """Fixture to create a test client for the Flask app."""
    return create_app.test_client()

@pytest.fixture
def mock_db(create_app):
    """Fixture to set up and tear down a mock database for testing."""
    with create_app.app_context():
        db = create_app.config['db']
        db.notes.insert_one({'title': 'Note Title', 'main_body': 'Test body'})
        yield db
        db.notes.delete_one({'title': 'Note Title'})

def test_show_main_screen(client):
    """Test showing the main screen."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Easy Note' in response.data

def test_capture_image(client):
    """Test the image capture screen."""
    response = client.get('/capture_image')
    assert response.status_code == 200
    assert b'<title>Add Course</title>' in response.data

def test_upload_image(client, create_app):
    """Test uploading an image."""
    valid_base64_image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='
    mock_image = {'imageData': valid_base64_image}
    response = client.post('/upload_image', json=mock_image)
    assert response.status_code == 200

def test_show_edit_note(client, mock_db):
    """Test showing the edit note screen."""
    test_title = 'Note Title'
    response = client.get(f'/show_edit_note?title={test_title}')
    assert response.status_code == 200
    assert b'Edit Notes' in response.data

def test_edit_note_confirm(client, create_app):
    """Test confirming an edited note."""
    test_title = 'Test Note Title'
    mock_note_data = {'title': 'New Title', 'main_body': 'New Body'}
    response = client.post(f'/edit_confirm/{test_title}', data=mock_note_data)
    assert response.status_code == 200
    assert b'Note Updated' in response.data

def test_delete_note(client):
    """Test deleting a note."""
    test_title = 'Note Title'
    response = client.get(f'/delete_note/{test_title}')
    assert response.status_code == 302

def test_show_all_notes(client):
    """Test showing all notes."""
    response = client.get('/show_all_notes')
    assert response.status_code == 200
    assert b'All Notes' in response.data

def test_show_search_notes(client):
    """Test showing the search notes screen."""
    response = client.get('/show_search_notes')
    assert response.status_code == 200
    assert b'Search' in response.data

def test_search_notes(client, create_app):
    """Test searching notes."""
    mock_search_data = {'keywords': 'Test Query'}
    response = client.post('/search', data=mock_search_data)
    assert response.status_code == 200
