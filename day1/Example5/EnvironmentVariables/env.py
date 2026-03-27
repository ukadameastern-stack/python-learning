import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    DEBUG: bool = os.environ.get("DEBUG", "False") == "True"
    DB_URL = os.environ.get("DB_URL", "sqlite:///default.db")

settings = Settings()

print(settings.SECRET_KEY)
print(settings.DEBUG)
print(settings.DB_URL)

'''
123456789
True
postgresql://user:pass@localhost:5432/db
'''