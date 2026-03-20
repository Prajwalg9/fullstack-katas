import requests
user = input("Enter the image name: ")
user_agent = {"User-Agent": "Mozilla/S. (Windous NT 10.0; Win64: X64) AppleWebKit/537-36 (KHTMLike Gecko Chrome/88.0.4324.150 Safari/537 36"}
url = f"https://www.google.com/search?q={user}&sounce=1nms&tbm=isch&sa=X&ved=2ahUKEwifxZKygebuAhUQ0SsKHc1ZDsFQ_AUoAXoECBs.QAw&biw=1536&bih=760"
response = requests.get(url=url, headers=user_agent).content
print(response)