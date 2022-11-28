import requests
import wget
import json
import urllib.request
import requests as req
import markdown # pip install markdown
from bs4 import BeautifulSoup # pip install beautifulsoup4
file_path = "/Users/yejin/Github-Tag-Embedder/github_crawling/READMEs.json"
def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

with open(file_path, 'r') as file:
    data = json.load(file)
    for key in data:
      data[key] = md_to_text(data[key])
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent="\t")

