from typing import Optional

class User:
    def __init__(self, name: str, email: Optional[str] = 'u@g.com'):
        self.name = name
        self.email = email

    def get_user(name1: Optional[str]) -> int:
        return name1 or "Guest"        

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})" 


u2 = User("uday")
print(User.get_user(None)) 
print(type(User.get_user(None))) 