import requests
username = None
print("Hello")
print(input("Username: ", username))

s = requests.Session()
s.get('https://www.facebook.com/{}', username)
print(requests.status_codes)