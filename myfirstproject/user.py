class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(uday):
        return f"User(id={uday.id}, name={uday.name}, email={uday.email})"

    # 🔹 CLASSMETHOD → Factory from API response
    @classmethod
    def from_api(cls, data: dict):
        return cls(
            id=data.get("user_id"),
            name=data.get("full_name"),
            email=data.get("email")
        )

    # 🔹 CLASSMETHOD → Factory from DB row
    @classmethod
    def from_db(cls, row: tuple):
        return cls(
            id=row[0],
            name=row[1],
            email=row[2]
        )

    # 🔹 STATICMETHOD → Utility validation
    @staticmethod
    def is_valid_email(email: str):
        return "@" in email and "." in email