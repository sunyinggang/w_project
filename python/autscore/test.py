import os

from werkzeug.security import generate_password_hash

pws = generate_password_hash("123456")
t = os.getcwd()
print(t)