import requests
username = input()

s = requests.Session()
s.get('https://www.facebook.com/{}', username)
print(requests.status_codes)