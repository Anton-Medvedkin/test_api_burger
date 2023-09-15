import pytest
import requests
import copy
import allure
from resources.config import *
from resources.constants import *

@allure.title("Changes to user data")
class TestChangingUserData:

 @allure.title("Changing user email")
 @allure.description("Checking that the email of the authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_user_email(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{def_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 @allure.title("Changing user password")
 @allure.description("Checking that the password of an authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_user_password(self, login_user):
    data = copy.deepcopy(json_data)
    data["password"] = "newPasswordUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{def_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 @allure.title("Changing user name")
 @allure.description("Checking that the name of the authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_user_name(self, login_user):
    data = copy.deepcopy(json_data)
    data["name"] = "newNameUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{def_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 @allure.title("Changing user all parameters")
 @allure.description("Checking that all the parameters of the authenticated user can be changed. Checking the status of the code and the response body.")
 def test_changing_user_all_parameters(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    data["password"] = "newPasswordUser"
    data["name"] = "newNameUser"
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{def_url}auth/user", headers=headers, data=data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)


@allure.title("Changing the data of an unauthenticated user")
class TestChangingDataUnauthenticatedUser:

 @allure.title("Changing the data of an unauthenticated user")
 @allure.description("Checking that it is possible to change all the parameters of an unauthenticated user. Checking the status of the code and the response body.")
 def test_changing_data_unauthenticated_user(self, login_user):
    data = copy.deepcopy(json_data)
    data["email"] = "newEmailUser"
    data["password"] = "newPasswordUser"
    data["name"] = "newNameUser"
    response = requests.patch(f"{def_url}auth/user", data=data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"



