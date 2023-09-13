import pytest
import requests
import copy
import allure
from resources.config import *

@allure.title("Data modification tests for an authenticated user")
class TestChangingDataAuthenticatedUser:

 @allure.title("Changing the email of an authenticated user")
 @allure.description("Checking that the email of the authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_email_authenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 @allure.title("Changing the password of an authenticated user")
 @allure.description("Checking that the password of an authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_password_authenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["password"] = "newPasswordUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 @allure.title("Changing the name of an authenticated user")
 @allure.description("Checking that the name of the authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_name_authenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["name"] = "newNameUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 @allure.title("Changing the all parameters of an authenticated user")
 @allure.description("Checking that all the parameters of the authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_all_parameters_authenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    data["password"] = "newPasswordUser"
    data["name"] = "newNameUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

@allure.title("Data modification tests for an unauthenticated user")
class TestChangingDataUnauthenticatedUser:

 @allure.title("Changing the email of an unauthenticated user")
 @allure.description("Checking that the email of an unauthenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_email_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 @allure.title("Changing the password of an unauthenticated user")
 @allure.description("Checking that the password of an unauthenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_password_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["password"] = "newPasswordUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 @allure.title("Changing the name of an unauthenticated user")
 @allure.description("Checking that the name of an unauthenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_name_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["name"] = "newNameUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 @allure.title("Changing the all parameters of an unauthenticated user")
 @allure.description("Checking that it is possible to change all the parameters of an unauthenticated user. Checking the status of the code and the response body.")
 def test_changing_all_parameters_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    data["password"] = "newPasswordUser"
    data["name"] = "newNameUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"



