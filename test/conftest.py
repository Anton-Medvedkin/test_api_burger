import pytest
import requests


@pytest.fixture()
def create_user(base_url):
    json_data = {
        "email": "test-кda3tjkh@yandex.ru",
        "password": "333к633553",
        "name": "3651515к3"
        }
    response = requests.post(f"{base_url}auth/register", data=json_data)
    yield response
    response_token = response.json()['accessToken']
    headers = {"authorization": response_token}
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=headers)


@pytest.fixture()
def login_user(create_user, base_url):
    json_data = {
        "email": "test-кda3tjkh@yandex.ru",
        "password": "333к633553"
    }
    response = requests.post(f"{base_url}auth/login", data=json_data)
    return response


@pytest.fixture()
def base_url():
    url = "https://stellarburgers.nomoreparties.site/api/"
    return url

