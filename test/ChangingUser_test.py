import pytest
import requests
import copy
import allure
from resources.config import *

class TestChangingDataAuthenticatedUser:

 @allure.title("Chahging email")
 @allure.description("Changing the email of an authenticated user")
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

 @allure.title("Chahging password")
 @allure.description("Changing the password of an authenticated user")
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

 @allure.title("Chahging name")
 @allure.description("Changing the name of an authenticated user")
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

 @allure.title("Chahging all parameters")
 @allure.description("Changing the all parameters of an authenticated user")
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

class TestChangingDataUnauthenticatedUser:

 @allure.title("Chahging email")
 @allure.description("Changing the email of an unauthenticated user")
 def test_changing_email_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 @allure.title("Chahging password")
 @allure.description("Changing the password of an unauthenticated user")
 def test_changing_password_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["password"] = "newPasswordUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 @allure.title("Chahging name")
 @allure.description("Changing the name of an unauthenticated user")
 def test_changing_name_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["name"] = "newNameUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 @allure.title("Chahging all parameters")
 @allure.description("Changing the all parameters of an unauthenticated user")
 def test_changing_all_parameters_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    data["password"] = "newPasswordUser"
    data["name"] = "newNameUser"
    response = requests.patch(f"{base_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"



