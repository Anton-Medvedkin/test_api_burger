import pytest
import requests
from resources.config import *


@pytest.fixture()
def create_user():
    response = requests.post(f"{base_url}auth/register", data=json_data)
    yield response
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete(f"{base_url}auth/user", headers=headers)


@pytest.fixture()
def login_user():
    requests.post(f"{base_url}auth/register", data=json_data)
    data = {key: json_data[key] for key in ["email", "password"]}
    response = requests.post(f"{base_url}auth/login", data=data)
    yield response
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete(f"{base_url}auth/user", headers=headers)








