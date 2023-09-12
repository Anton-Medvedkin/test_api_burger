import pytest
import requests

def test_receipt_order_using_authenticated(login_user, base_url):
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.get(f"{base_url}orders", headers=headers)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['total'] is not None
    assert response.json()['totalToday'] is not None

def test_receipt_order_not_using_authenticated(base_url):
    response = requests.get(f"{base_url}orders")
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"
