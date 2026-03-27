class User:
    count = 0   # class variable (shared across all instances)

    def __init__(self):
        User.count += 1   # increment on every object creation

    @classmethod
    def get_count(cls):
        return cls.count
    

u1 = User()
u2 = User()

print(User.count)  # 2

'''
@classmethod → Why used?
-------------------------

    @classmethod
    def get_count(cls):
        return cls.count

Key idea:
    - cls refers to the class itself (not instance)
    - Works even with inheritance

Why not use a normal method?
----------------------------

If you wrote:

    def get_count(self):
        return self.count

Problems:

    - Requires an instance
    - Conceptually wrong (count belongs to class, not object)

Why not use @staticmethod?
---------------------------

You could, but:

    @staticmethod
    def get_count():
        return User.count
        
❌ Hardcoded class name
❌ Breaks inheritance flexibility        

'''