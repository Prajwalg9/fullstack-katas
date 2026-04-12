import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=smartphones+under+20000"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

res = requests.get(url, headers=headers)

print("Status:", res.status_code)

soup = BeautifulSoup(res.text, "html.parser")

items = soup.select(".s-result-item")

print("Items found:", len(items))

for item in items[:5]:
    title = item.select_one("h2")
    if title:
        print(title.text.strip())