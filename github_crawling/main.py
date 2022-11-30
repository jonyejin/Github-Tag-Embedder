import requests
import wget
import json
import urllib.request
import requests as req
import markdown # pip install markdown
from bs4 import BeautifulSoup # pip install beautifulsoup4

# token = "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" #d원후
# token = "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" # 치현
# "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" # yejin
# token = "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"
# token = "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" # yejin another
# token = "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" # yejin another
token = "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" # yejin new
headers = {
            "Authorization": "token " + token,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/84.0.4147.89 Safari/537.36"}
my_json = {}
urls = [
  "https://github.com/keras-team/keras",
]

# yejin: id와 repo_name을 넣으면 파싱된 결과를 리턴해줌
def whole_func(repo_urls, headers):
    for repo_url in repo_urls:
      url_dict = {"login": repo_url.split("/")[3], "repo_name": repo_url.split("/")[4]}
      topics = get_repository_infos(url_dict["login"], url_dict["repo_name"], headers)
      get_repository_README(url_dict["login"], url_dict["repo_name"], topics)
      with open('READMEs.json', 'w', encoding='utf-8') as make_file:
          json.dump(my_json, make_file, indent="\t")

# topic의 string array를 리턴한다.
def get_repository_infos(login, repo_name, headers):
    base_url = f"https://api.github.com/repos/{login}/{repo_name}"
    print(base_url)
    res = requests.get(base_url, headers=headers)
    res.raise_for_status()

    data = res.json()
    # print(data["topics"])
    return data["topics"]

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

def get_repository_README(login, repo_name, topics):
    # status code 확인하기
    r1 = f"https://github.com/{login}/{repo_name}/raw/master/README.md"
    r2 = f"https://raw.githubusercontent.com/{login}/{repo_name}/main/README.md"
    test_r1 = requests.get(r1)
    test_r2 = requests.get(r2)

    if test_r1.status_code == 200:
      print(r1)
      with urllib.request.urlopen(r1) as f:
        body = f.read().decode('utf-8')
        my_json[" ".join(topics)] = md_to_text(body)

    elif test_r2.status_code == 200:
      print(r2)
      with urllib.request.urlopen(r2) as f:
        body = f.read().decode('utf-8')
        my_json[" ".join(topics)] = md_to_text(body)
    else:
      print("parse 실패")
whole_func(urls, headers)     
