import requests
import config

url = config.user()
name = input("Enter your name: ")
email = input("Enter your email: ")
status = input("Enter your status: ")
gender = input("Enter your gender: ")

data = dict()

data['name'] = name
data['email'] = email
data['status'] = status
data['gender'] = gender

r = requests.post(url, data = data)
print(r)