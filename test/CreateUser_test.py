import pytest
import requests

def test_creating_a_unique_user(create_user):
    assert create_user.status_code == 200
    assert create_user.json()['success'] == True

def test_сreating_user_using_data_already_available_in_database(base_url, create_user):
    json_data = {
        "email": "test-кda3tjkh@yandex.ru",
        "password": "333к633553",
        "name": "3651515к3"
    }
    response = requests.post(f"{base_url}auth/register", data=json_data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "User already exists"



class TestCreatingUserNotUsingParameter:

 def test_сreating_user_not_using_email(self, base_url):
    json_data = {
        "password": "333к6333",
        "name": "365к3"
    }
    response = requests.post(f"{base_url}auth/register", data=json_data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 def test_сreating_user_not_using_password(self, base_url):
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "name": "365к3"
    }
    response = requests.post(f"{base_url}auth/register", data=json_data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 def test_сreating_user_not_using_name(self, base_url):
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "password": "333к6333"
    }
    response = requests.post(f"{base_url}auth/register", data=json_data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"