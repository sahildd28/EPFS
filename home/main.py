from re import template
from bs4 import BeautifulSoup

with open('C:/Users/sahil/Documents/CODING/Pythong/hello/templates/index.html','r') as main_html:
    content=main_html.read()
    soup=BeautifulSoup(content,'lxml')
    h1_tags=soup.findAll('h1')
    for i in h1_tags:
        print(i.text)


