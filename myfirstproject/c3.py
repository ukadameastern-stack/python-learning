from user import User

# 1. From API
api_data = {
    "user_id": 101,
    "full_name": "Uday Kadam",
    "email": "uday@gmail.com"
}

user1 = User.from_api(api_data)
print(user1) # User(id=101, name=Uday Kadam, email=uday@gmail.com)

# # 2. From DB
db_row = (102, "Rahul Sharma", "rahul@gmail.com")

user2 = User.from_db(db_row)
print(user2) # User(id=102, name=Rahul Sharma, email=rahul@gmail.com)

# # 3. Email Validation
print(User.is_valid_email("test@gmail.com"))   # True
print(User.is_valid_email("invalid-email"))    # False


'''
User(id=101, name=Uday Kadam, email=uday@gmail.com)
User(id=102, name=Rahul Sharma, email=rahul@gmail.com)
True
False
'''