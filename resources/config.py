import random
import string

# JSON используемый в тестах для создания нового рандомного пользователя
json_data = {
            "email": "".join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@example.com",
            "password": "".join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            "name": "".join(random.choices(string.ascii_lowercase, k=5))
        }



