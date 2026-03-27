class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"

    def __str__(self):
        return f"{self.name} ({self.email})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)
    
u1 = User("A", "a@mail.com")
u2 = User("A", "a@mail.com")
u3 = u2

print(u1 == u2)   # True ✅ (__eq__)
print(u1 is u2)   # False ❌ (different objects)  
print(u3 == u2)   # True ✅ (__eq__)
print(u3 is u2)   # True ✅  