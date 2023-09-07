import pytest
import requests

def test_changing_with_authorization(login_user):
    json_data = {
        "email": "newEmail",
        "password": "newPassword",
        "name": "newName"
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.patch("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers, data=json_data)
    assert response.status_code == 200
    assert response.json()['success'] == True

def test_changing_without_authorization(login_user):
    json_data = {
        "email": "newEmail",
        "password": "newPassword",
        "name": "newName"
    }
    response = requests.patch("https://stellarburgers.nomoreparties.site/api/auth/user", data=json_data)
    assert response.status_code == 401
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"



