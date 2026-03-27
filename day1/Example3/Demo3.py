
class User:
    count = 0   # class variable (shared across all instances)

    def __init__(self):
        #type(self).count += 1    # ✅ dynamic class reference
        self.__class__.count += 1 # ✅ dynamic class reference

    @classmethod
    def get_count(cls):
        return cls.count

class Admin(User):
    count = 0

a1 = Admin()
a2 = Admin()

print(Admin.get_count())  # 2
print(User.get_count())   # 0