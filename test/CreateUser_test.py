import pytest
import requests
from resources.config import *


def test_creating_a_unique_user(create_user):
    assert create_user.status_code == 200
    assert create_user.json()['success'] == True

def test_сreating_user_using_data_already_available_in_database(create_user):
    response = requests.post(f"{base_url}auth/register", data=json_data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "User already exists"



class TestCreatingUserNotUsingParameter:

 def test_сreating_user_not_using_email(self):
    data = {key: json_data[key] for key in ["name", "password"]}
    response = requests.post(f"{base_url}auth/register", data=data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 def test_сreating_user_not_using_password(self):
    data = {key: json_data[key] for key in ["email", "name"]}
    response = requests.post(f"{base_url}auth/register", data=data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 def test_сreating_user_not_using_name(self):
    data = {key: json_data[key] for key in ["email", "password"]}
    response = requests.post(f"{base_url}auth/register", data=data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"