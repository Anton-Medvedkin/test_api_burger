import random
import string

json_data = {
            "email": "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com",
            "password": "".join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            "name": "".join(random.choices(string.ascii_lowercase, k=5))
        }

json_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71"]
    }

base_url = "https://stellarburgers.nomoreparties.site/api/"