import requests

url='http://127.0.0.1:8000/posts/'
user='viru'
password='viruGG99@'
payload=[]
for i in range(1,20,2):
    payload.append({'title':f'This is title number {i}', 'content':f'This is content number {i}', 'published':False})
    payload.append({'title':f'This is title number {i+1}', 'content':f'This is content number {i+1}', 'published':True})   
for i in payload:
    response=requests.post(url=url, data=i, auth=(user, password))
    print(response.text)