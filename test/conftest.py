import pytest
import requests


@pytest.fixture()
def create_user():
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "password": "333к6333",
        "name": "365к3"
        }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=json_data)
    yield response
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)


@pytest.fixture()
def login_user(create_user):
    json_data = {
        "email": "test-кda3t6a@yandex.ru",
        "password": "333к6333"
    }
    response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", data=json_data)
    return response

@pytest.fixture()
def base_url():
    url = "https://stellarburgers.nomoreparties.site/api/"
    return url

