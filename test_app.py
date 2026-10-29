import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_celsius_conversion(client):
    res = client.get('/c-to-f?celsius=0')
    assert res.json['output_fahrenheit'] == 32.0

def test_fahrenheit_conversion(client):
    res = client.get('/f-to-c?fahrenheit=32')
    assert res.status_code == 200
    assert res.json['output_celsius'] == 0.0
