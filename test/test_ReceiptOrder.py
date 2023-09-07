import pytest
import requests

def test_create_order_with_authorization_and_ingredients(login_user):
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.get("https://stellarburgers.nomoreparties.site/api/orders", headers=headers)
    assert response.status_code == 200
    assert response.json()['success'] == True

def test_create_order_without_authorization_and_ingredients():
    response = requests.get("https://stellarburgers.nomoreparties.site/api/orders")
    assert response.status_code == 401
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"
