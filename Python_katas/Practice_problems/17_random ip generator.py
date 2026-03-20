import random

def random_ip():
    return '.'.join(str(random.randint(0,255)) for i in range(4))

Ip_s=[random_ip() for _ in range(1000)]

with open("ip.txt","w") as f:
    for ip in Ip_s:
        f.write(ip+"\n")
