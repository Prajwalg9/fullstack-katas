import requests

url='http://127.0.0.1:8000/posts/'
user='viru'
password='viruGG99@'

response=requests.get(url=url, params={'limit':5, 'offset':10}, auth=(user, password))

print(response.json())