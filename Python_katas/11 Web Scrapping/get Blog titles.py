import requests
from bs4 import BeautifulSoup

def get_blog_titles(url):
    response=requests.get(url=url).content
    soup=BeautifulSoup(response, 'lxml')
    tag=soup.find('td', {id:'mp-tfa'})
    print(tag)
    
get_blog_titles('https://en.wikipedia.org/wiki/Main_Page')