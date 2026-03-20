import re

with open("raw ip.txt","r", encoding="utf-8", errors="replace") as f:
    data=f.read()

pattern=r"\d{1,3}(?:\.\d{1,3}){1,3}"
matches=re.findall(pattern,data)

# ip = []
# for item in matches:
#     chars=list(item.split("."))
#     if len(chars)==4:
#         print(chars)
def validator(Data):
    ip = []
    for item in Data:
        chars=list(item.split("."))
        if len(chars)==4 and (int(chars[0]) <= 255 and int(chars[1]) <= 255 and int(chars[2]) <= 255 and int(chars[3]) <= 255):
            ip.append(item)
    return ip
print(validator(matches))