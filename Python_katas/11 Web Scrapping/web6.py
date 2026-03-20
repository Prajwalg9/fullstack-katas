import requests
import re
import os

user = input("Enter the image name: ")
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
url = f"https://www.google.com/search?q={user}&udm=2"

if not os.path.exists(user):
    os.makedirs(user)

response = requests.get(url=url, headers=user_agent).text
pattern = r"https://[^\"']+\.(?:jpg|jpeg|png)"
all_links = re.findall(pattern, response)

unique_images = []
for link in all_links:
    if link not in unique_images and "gstatic.com" not in link:
        unique_images.append(link)

count = 0
for link in unique_images:
    if count == 5:
        break
    try:
        img_data = requests.get(link, timeout=5).content
        with open(f"{user}/image_{count+1}.jpg", "wb") as f:
            f.write(img_data)
        print(f"✅ Saved Unique: {link}")
        count += 1
    except:
        continue