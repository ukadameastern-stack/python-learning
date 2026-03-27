import os

class Settings:
    DB_URL: str = os.environ.get("DB_URL")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    DEBUG: bool = os.environ.get("DEBUG", "False") == "True"
    PORT: int = int(os.environ.get("PORT", 8000))
    PAYMENT_MODE: str = os.environ.get("PAYMENT_MODE", "test")

print(Settings.DB_URL)          # None  
print(Settings.SECRET_KEY)      # None
print(Settings.DEBUG)           # False
print(Settings.PORT)            # 8000
print(Settings.PAYMENT_MODE)    # test