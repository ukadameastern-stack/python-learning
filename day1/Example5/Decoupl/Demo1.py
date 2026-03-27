from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)

print(SECRET_KEY)
print(DEBUG)

'''
abc123
True

'''