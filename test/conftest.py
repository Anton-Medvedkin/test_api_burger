import pytest
import requests
import random
from resources.config import *
from resources.constants import *

@pytest.fixture()
def create_user():
    response = requests.post(f"{def_url}auth/register", data=json_data)
    yield response
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete(f"{def_url}auth/user", headers=headers)


@pytest.fixture()
def login_user():
    requests.post(f"{def_url}auth/register", data=json_data)
    data = {key: json_data[key] for key in ["email", "password"]}
    response = requests.post(f"{def_url}auth/login", data=data)
    yield response
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete(f"{def_url}auth/user", headers=headers)

@pytest.fixture()
def create_ingredients():
    response = requests.get("https://stellarburgers.nomoreparties.site/api/ingredients")
    ids = [item['_id'] for item in response.json()['data']]
    random_ids = random.sample(ids, 2)
    json_ingredients = {
        "ingredients": random_ids
    }
    return json_ingredients






