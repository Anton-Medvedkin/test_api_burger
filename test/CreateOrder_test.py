import pytest
import requests
import copy
from resources.config import *

class TestOrderUsingAuthenticatedUser:

 def test_creating_order_using_authenticated_user_and_ingredients(self, login_user):
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{base_url}orders", headers=headers, data=json_ingredients)
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['name'] is not None
    assert response.json()['order'] is not None


 def test_creating_order_using_authenticated_user_and_not_using_ingredients(self, login_user):
    data = {}
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{base_url}orders", headers=headers, data=data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"

 def test_creating_order_using_authenticated_user_and_using_invalid_ingredients(self, login_user):
    data = copy.deepcopy(json_ingredients)
    data["ingredients"] = ["1", "2"]
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{base_url}orders", headers=headers, data=data)
    assert response.status_code == 500, "It didn't return the response code we were expecting."


class TestOrderNotUsingAuthenticatedUser:

 def test_creating_order_not_using_authenticated_user_and_using_ingredients(self):
    response = requests.post(f"{base_url}orders", data=json_ingredients)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True


 def test_creating_order_not_using_authenticated_user_and_not_using_ingredients(self):
    data = {}
    response = requests.post(f"{base_url}orders", data=data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"

 def test_creating_order_not_using_authenticated_user_and_using_invalid_ingredients(self, login_user):
    data = copy.deepcopy(json_ingredients)
    data["ingredients"] = ["1", "2"]
    response = requests.post(f"{base_url}orders", data=data)
    assert response.status_code == 500, "It didn't return the response code we were expecting."