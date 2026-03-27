from Admin import Admin
from User import User


user = User("Balaji", "b@g.com");
print("============From User============")
print(user.name)
print(user.email)

'''
============From User============
Balaji
b@g.com
'''

admin = Admin("Udaysinh Kadam", "u@email.com", "Admin")
print("============From Admin============")
print(admin.name)
print(admin.email)
print(admin.role)

'''
============From Admin============
Udaysinh Kadam
u@email.com
Admin
'''
