import pytest
import requests
import allure
from resources.config import *

@allure.title("Creating a unique user")
@allure.description("Checking the possibility of creating a new user who was not in the database. Checking the status of the code and the response body")
def test_creating_a_unique_user(create_user):
    assert create_user.status_code == 200
    assert create_user.json()['success'] == True

@allure.title("Creating a previously registered user")
@allure.description("Checking the impossibility of creating a previously registered user. Checking the status of the code and the response body")
def test_сreating_user_using_data_already_available_in_database(create_user):
    response = requests.post(f"{base_url}auth/register", data=json_data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "User already exists"


@allure.title("Testing creating a user not using parameters")
class TestCreatingUserNotUsingParameter:

 @allure.title("Creating a user not using an email")
 @allure.description("Checking that a user cannot be created not using an email. Checking the status of the code and the response body")
 def test_сreating_user_not_using_email(self):
    data = {key: json_data[key] for key in ["name", "password"]}
    response = requests.post(f"{base_url}auth/register", data=data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 @allure.title("Creating a user not using an password")
 @allure.description("Checking that a user cannot be created not using an password. Checking the status of the code and the response body")
 def test_сreating_user_not_using_password(self):
    data = {key: json_data[key] for key in ["email", "name"]}
    response = requests.post(f"{base_url}auth/register", data=data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"

 @allure.title("Creating a user not using an name")
 @allure.description("Checking that a user cannot be created not using an name. Checking the status of the code and the response body")
 def test_сreating_user_not_using_name(self):
    data = {key: json_data[key] for key in ["email", "password"]}
    response = requests.post(f"{base_url}auth/register", data=data)
    assert response.status_code == 403, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Email, password and name are required fields"