import pytest
import requests

class TestOrderUsingAuthenticatedUser:

 def test_creating_order_using_authenticated_user_and_ingredients(self, login_user, base_url):
    json_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{base_url}orders", headers=headers, data=json_data)
    assert response.status_code == 200
    assert response.json()['success'] == True
    assert response.json()['name'] is not None
    assert response.json()['order'] is not None


 def test_creating_order_using_authenticated_user_and_not_using_ingredients(self, login_user, base_url):
    json_data = {
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{base_url}orders", headers=headers, data=json_data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"

 def test_creating_order_using_authenticated_user_and_using_invalid_ingredients(self, login_user, base_url):
    json_data = {
        "ingredients": ["1", "2"]
    }
    response_token = login_user.json()['accessToken']
    headers = {"authorization": response_token}
    response = requests.post(f"{base_url}orders", headers=headers, data=json_data)
    assert response.status_code == 500, "It didn't return the response code we were expecting."


class TestOrderNotUsingAuthenticatedUser:

 def test_creating_order_not_using_authenticated_user_and_using_ingredients(self, base_url):
    json_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    }
    response = requests.post(f"{base_url}orders", data=json_data)
    assert response.status_code == 200, "It didn't return the response code we were expecting."
    assert response.json()['success'] == True


 def test_creating_order_not_using_authenticated_user_and_not_using_ingredients(self, base_url):
    json_data = {
    }
    response = requests.post(f"{base_url}orders", data=json_data)
    assert response.status_code == 400, "It didn't return the response code we were expecting."
    assert response.json()['success'] == False
    assert response.json()['message'] == "Ingredient ids must be provided"

 def test_creating_order_not_using_authenticated_user_and_using_invalid_ingredients(self, login_user, base_url):
    json_data = {
        "ingredients": ["1", "2"]
    }
    response = requests.post(f"{base_url}orders", data=json_data)
    assert response.status_code == 500, "It didn't return the response code we were expecting."