import json
from app import app

def test_easy_word():
    tester = app.test_client()
    response = tester.post('/get_word', json={"difficulty": "easy"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "word" in data
