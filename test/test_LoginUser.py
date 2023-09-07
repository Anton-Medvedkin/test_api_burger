import pytest
import requests

def test_log_in_as_an_existing_user(login_user):
    assert login_user.status_code == 200, f"Status code 200 was expected and code {login_user.status_code} was returned."
    assert login_user.json()['success'] == True

def test_log_in_as_a_non_existent_user():
    json_data = {
        "email": "none",
        "password": "none"
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", data=json_data)
    assert response.status_code == 401, f"Status code 401 was expected and code {response.status_code} was returned."
    assert response.json()['success'] == False
    assert response.json()['message'] == "email or password are incorrect"