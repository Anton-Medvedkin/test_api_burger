import pytest
import requests

class TestOrderWithAuthorization:

 def test_create_order_with_authorization_and_ingredients(self, login_user):
    json_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders", headers=headers, data=json_data)
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['name']
    assert response.json()['order']


 def test_create_order_with_authorization_without_ingredients(self, login_user):
    json_data = {
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders", headers=headers, data=json_data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"


class TestOrderWithoutAuthorization:

 def test_create_order_without_authorization_and_ingredients(self):
    json_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders", data=json_data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True



 def test_create_order_without_authorization_without_ingredients(self):
    json_data = {
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders", data=json_data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"

class TestOrderWithInvalidIngredients:

 def test_create_order_with_invalid_ingredients(self, login_user):
    json_data = {
        "ingredients": ["1", "2"]
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post("https://stellarburgers.nomoreparties.site/api/orders", headers=headers, data=json_data)
    assert response.status_code == 500, "It didn't return the response code we were expecting."