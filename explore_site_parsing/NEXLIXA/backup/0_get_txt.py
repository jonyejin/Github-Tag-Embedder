import requests
from bs4 import BeautifulSoup as bs

url = "https://github.com/topics/data-science"
response = requests.get(url)
soup = bs(response.text, 'lxml')

with open('./main_raw.txt', 'w') as file:
    file.write(soup.get_text())

#nameList = map(bs.get_text, bsObj.findAll("li", {""}))

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

