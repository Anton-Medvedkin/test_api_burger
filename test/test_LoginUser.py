import pytest
import requests

def test_log_in_as_an_existing_user(login_user):
    assert login_user.status_code == 200, "It didn't return the response code we were expecting."
    assert login_user.json()['success'] == True
    assert login_user.json()['accessToken']
    assert login_user.json()['refreshToken']
    assert login_user.json()['user']

def test_log_in_as_a_non_existent_user():
    json_data = {
        "email": "none",
        "password": "none"
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", data=json_data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "email or password are incorrect"