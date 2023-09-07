import pytest
import requests

def test_creating_a_unique_user(create_user, base_url):
    assert create_user.status_code == 200
    assert create_user.json()['success'] == True

def test_сreating_a_non_unique_user(create_user, base_url):
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "password": "333к6333",
        "name": "365к3"
    }
    response = requests.post(f"{base_url} + auth/register", data=json_data)
    assert response.status_code == 403, f"Status code 200 was expected and code {create_user.status_code} was returned."
    assert response.json()['success'] == False
    assert response.json()['message'] == "User already exists"

class TestCreatingUserWithoutParameter:

 def test_сreating_user_without_email(self):
    json_data = {
        "password": "333к6333",
        "name": "365к3"
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=json_data)
    assert response.status_code == 403, f"Status code 200 was expected and code {response.status_code} was returned."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 def test_сreating_user_without_password(self):
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "name": "365к3"
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=json_data)
    assert response.status_code == 403, f"Status code 200 was expected and code {response.status_code} was returned."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 def test_сreating_user_without_name(self):
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "password": "333к6333"
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=json_data)
    assert response.status_code == 403, f"Status code 200 was expected and code {response.status_code} was returned."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"