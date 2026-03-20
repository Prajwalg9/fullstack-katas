import requests
from bs4 import BeautifulSoup

def Extract(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    response = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(response, 'lxml')
    headers_found = soup.find_all("h2")

    if headers_found:
        print(f"Found {len(headers_found)} sections!\n")
        content = [h.get_text(strip=True) for h in headers_found]
        
        for index, text in enumerate(content, 1):
            print(f"{index}. {text}")
    else:
        print("Still couldn't find any h2 tags. Wikipedia might be blocking the request.")

Extract("https://en.wikipedia.org/wiki/Main_Page")