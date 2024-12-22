import requests
username = input()
print("Username: ")
s = requests.Session()
s.get('https://www.facebook.com/{}', username)
print(requests.status_codes)