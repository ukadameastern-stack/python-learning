from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int = 18


u = User("Uday", "u@g.com", 25) # __init__  
print(u)                        # __repr__
# User(name='Uday', email='u@g.com', age=25)

u2 = u

print(u2 == u) # True
print(u2 is u) # True

u3 = User("Uday", "u@g.com", 25)

print(u3 == u2) # True
print(u3 is u2) # False