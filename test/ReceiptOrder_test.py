import pytest
import requests
import allure
from resources.config import *
from resources.constants import *

@allure.title("Receiving an order from an authenticated user")
@allure.description("Verifying that an authenticated user's order can be received. Checking the status of the code and the response body")
def test_receipt_order_using_authenticated(login_user):
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.get(f"{def_url}orders", headers=headers)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True
    assert response.json()['total'] is not None
    assert response.json()['totalToday'] is not None

@allure.title("Receiving an order from an unauthenticated user")
@allure.description("Checking that it is impossible to receive an order from an unauthenticated user. Checking the status of the code and the response body")
def test_receipt_order_not_using_authenticated():
    response = requests.get(f"{def_url}orders")
    assert response.status_code == 401, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "You should be authorised"
