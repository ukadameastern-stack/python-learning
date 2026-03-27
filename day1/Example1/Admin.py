from User import User


class Admin(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role

