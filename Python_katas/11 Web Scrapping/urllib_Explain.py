import urllib.request, urllib.parse, urllib.error

url=urllib.request.urlopen('https://www.youtube.com/')

for line in url:
    line=line.decode('utf-8')
    print(f"{line.strip()}\n")
