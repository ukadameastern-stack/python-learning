from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int

user: UserDict = {
    "name", "Uday",
    "age", 25
}

print(user)
# {'name': 'Uday', 'age': 25}

'''
👉 Why not dataclass?

Use TypedDict → when working with JSON/dict
Use dataclass → when working with objects

'''

