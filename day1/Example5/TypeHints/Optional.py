
'''
🔷 1. Optional → value may be present or None
📌 Real use case: User profile API
'''

from typing import Optional

class User:
    def __init__(self, name: str, email: Optional[str] = None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"      
        
'''        
✅ Why?
Email may not be provided during signup
So type is: str OR None

👉 Equivalent:

Optional[str] == Union[str, None]
'''
print('===============Default value is Null==============')
u = User("uday")
print(u) 
# User(name='uday', email=None)

class User2:
    def __init__(self, name: str, email: Optional[str] = 'u@g.com'):
        self.name = name
        self.email = email        

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})" 


print('===============Default value is u@g.com==============')
u2 = User2("uday")
#print(u2)    
print(u2.get_user())    
# User(name='uday', email='u@g.com')

class User3:
    def __init__(self, name: str, email: Optional[str]):
        self.name = name
        self.email = email or "k@g.com"

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})" 


#u3 = User3("uday")
# TypeError: __init__()
# missing 1 required positional argument: 'email'