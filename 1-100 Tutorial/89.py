'''Requests module 
1.) Get Request
2.) Post Request'''

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)
  
# response = requests.get("https://www.google.com")
# print(response.text)


# url = "https://api.example.com/login"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Content-Type": "application/json"
# }
# data = {
#     "username": "myusername",
#     "password": "mypassword"
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)