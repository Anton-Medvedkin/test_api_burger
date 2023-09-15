import pytest
import requests
import copy
import allure
from resources.config import *
from resources.constants import *

@allure.title("Creating an order")
class TestCreatingOrder:

 @allure.title("Creating an order with ingredients")
 @allure.description("Verifying that an authenticated user can place an order by selecting ingredients")
 def test_creating_order_with_ingredients(self, login_user, create_ingredients):
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{def_url}orders", headers=headers, data=create_ingredients)
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['name'] is not None
    assert response.json()['order'] is not None


 @allure.title("Creating an order without ingredients")
 @allure.description("Checking that an authenticated user cannot place an order without selecting ingredients")
 def test_creating_order_without_ingredients(self, login_user):
    data = {}
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{def_url}orders", headers=headers, data=data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"

 @allure.title("Creating an order with an invalid hash")
 @allure.description("Verifying that an authenticated user cannot place an order by specifying the wrong ingredients")
 def test_creating_order_with_invalid_hash(self, login_user, create_ingredients):
    data = copy.deepcopy(create_ingredients)
    data["ingredients"] = ["1", "2"]
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{def_url}orders", headers=headers, data=data)
    assert response.status_code == 500, "It didn't return the response code we were expecting."

 @allure.title("Creation of an order by a non-authenticated user")
 @allure.description("Checking that an un-authenticated user can place an order by selecting ingredients")
 def test_creating_order_by_non_authenticated_user(self, create_ingredients):
    response = requests.post(f"{def_url}orders", data=create_ingredients)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True

