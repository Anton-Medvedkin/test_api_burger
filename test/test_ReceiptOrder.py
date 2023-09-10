import pytest
import requests

def test_receipt_order_with_authorization(login_user):
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.get("https://stellarburgers.nomoreparties.site/api/orders", headers=headers)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['total']
    assert response.json()['totalToday']

def test_receipt_order_without_authorization():
    response = requests.get("https://stellarburgers.nomoreparties.site/api/orders")
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"
