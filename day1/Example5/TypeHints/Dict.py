from typing import Dict

def get_user_data() -> Dict[str, str]:
    return {
        "name": "Uday",
        "email": "uday@gmail.com"
    }

print(get_user_data())

# {'name': 'Uday', 'email': 'uday@gmail.com'}