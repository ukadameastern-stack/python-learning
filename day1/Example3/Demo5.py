class User:
    def __init__(self, age):
        self._age = age   # internal (protected) attribute

    @property
    def age(self):
        return self._age
    
u = User(25)
print(u.age)     
# print(u.age()) # Without @property it will work like normal function 
# but with @property if we call like function then 
# it will give: TypeError: 'int' object is not callable