
class User:
    count = 0   # class variable (shared across all instances)

    def __init__(self):
        User.count += 1   # increment on every object creation

    @classmethod
    def get_count(cls):
        return cls.count

class Admin(User):
    count = 0

a1 = Admin()
a2 = Admin()

print(Admin.get_count())  # 0
print(User.get_count())   # 2