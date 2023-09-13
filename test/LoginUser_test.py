import pytest
import requests
import copy
import allure
from resources.config import *

@allure.title("Login of the registered user")
@allure.description("Checking that a previously registered user can log in. Checking the status of the code and the response body")
def test_login_registered_user(login_user):
    assert login_user.status_code == 200, "It didn't return the response code we were expecting."
    assert login_user.json()['success'] == True
    assert login_user.json()['accessToken'] is not None
    assert login_user.json()['refreshToken'] is not None
    assert login_user.json()['user'] is not None

@allure.title("User logging tests using invalid data")
class TestLoginUsingInvalidParameter:

 @allure.title("Logging a user using a invalid email")
 @allure.description("Checking that it is impossible to log in a user with an incorrect email. Checking the status and body of the response")
 def test_user_login_using_invalid_email(self):
    data = copy.deepcopy(json_data)
    data["email"] = "none"
    json = {key: data[key] for key in ["email", "password"]}
    response = requests.post(f"{base_url}auth/login", data=json)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "email or password are incorrect"

 @allure.title("Logging a user using a invalid password")
 @allure.description("Checking that it is impossible to log in a user with an incorrect password. Checking the status and body of the response")
 def test_user_login_using_invalid_password(self):
    data = copy.deepcopy(json_data)
    data["password"] = "none"
    json = {key: data[key] for key in ["email", "password"]}
    response = requests.post(f"{base_url}auth/login", data=json)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "email or password are incorrect"

 @allure.title("Logging a user using a invalid email and password")
 @allure.description("Checking that it is impossible to log in a user with an incorrect email and password. Checking the status and body of the response")
 def test_user_login_using_invalid_email_and_password(self):
    data = copy.deepcopy(json_data)
    data["email"] = "none"
    data["password"] = "none"
    json = {key: data[key] for key in ["email", "password"]}
    response = requests.post(f"{base_url}auth/login", data=json)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "email or password are incorrect"