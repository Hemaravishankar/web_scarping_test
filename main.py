from bs4 import BeautifulSoup
import requests
import re

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

name = soup.find(string=re.compile("David Marks"))
email = soup.find(string=re.compile("david"))
html = "".join(name.strip())
print(f'Name is ---- {html}')
print(f'Email id is ---- {email}')


