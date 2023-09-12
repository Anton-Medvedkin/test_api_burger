import pytest
import requests

class TestChangingDataAuthenticatedUser:

 def test_changing_email_authenticated_user(self, login_user, base_url):
    json_data = {
        "email": "newEmailUser",
        "password": "333к633553",
        "name": "3651515к3"
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=json_data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 def test_changing_password_authenticated_user(self, login_user, base_url):
    json_data = {
        "email": "test-кda3tjkh@yandex.ru",
        "password": "nawPasswordUser",
        "name": "3651515к3"
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=json_data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 def test_changing_name_authenticated_user(self, login_user, base_url):
    json_data = {
        "email": "test-кda3tjkh@yandex.ru",
        "password": "333к633553",
        "name": "newNameUser"
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=json_data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

 def test_changing_all_parameters_authenticated_user(self, login_user, base_url):
    json_data = {
        "email": "newEmailUser",
        "password": "newPasswordUser",
        "name": "newNameUser"
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch(f"{base_url}auth/user", headers=headers, data=json_data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['user'] is not None
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)

class TestChangingDataUnauthenticatedUser:

 def test_changing_email_unauthenticated_user(self, login_user, base_url):
    json_data = {
         "email": "newEmailUser",
         "password": "333к633553",
         "name": "3651515к3"
    }
    response = requests.patch(f"{base_url}auth/user", data=json_data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 def test_changing_password_unauthenticated_user(self, login_user, base_url):
    json_data = {
         "email": "test-кda3tjkh@yandex.ru",
         "password": "nawPasswordUser",
         "name": "3651515к3"
    }
    response = requests.patch(f"{base_url}auth/user", data=json_data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 def test_changing_name_unauthenticated_user(self, login_user, base_url):
    json_data = {
         "email": "test-кda3tjkh@yandex.ru",
         "password": "333к633553",
         "name": "newNameUser"
    }
    response = requests.patch(f"{base_url}auth/user", data=json_data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"

 def test_changing_all_parameters_unauthenticated_user(self, login_user, base_url):
    json_data = {
         "email": "newEmailUser",
         "password": "newPasswordUser",
         "name": "newNameUser"
    }
    response = requests.patch(f"{base_url}auth/user", data=json_data)
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"



