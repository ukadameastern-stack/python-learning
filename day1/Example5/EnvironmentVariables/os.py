import os
import json

db_url = os.environ.get("DB_URL", "https://xyz")
db_psw = os.environ.get("DB_PASSWORD", "1")
user = os.environ.get("USER", "xyz")

print(db_url)
print(db_psw)
print(user)

'''
How you set environment variables

🖥️ Linux: Run this command

export DB_PASSWORD=secret123
export DEBUG=True

'''
#print(json.dumps(dict(os.environ), indent=4))