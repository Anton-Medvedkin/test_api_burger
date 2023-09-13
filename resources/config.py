import random
import string

# JSON используемый в тестах для создания нового рандомного пользователя
json_data = {
            "email": "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com",
            "password": "".join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            "name": "".join(random.choices(string.ascii_lowercase, k=5))
        }

# JSON используемый для создания заказа
json_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    }

# Базовый url используемый для тестов
base_url = "https://stellarburgers.nomoreparties.site/api/"