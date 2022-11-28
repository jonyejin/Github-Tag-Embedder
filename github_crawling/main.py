import requests
import wget
import json
import urllib.request
import requests as req


# token = "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" #d원후
# token = "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" # 치현
# "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" # yejin
token = "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"
headers = {"Authorization": "token " + token,
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/84.0.4147.89 Safari/537.36"}
my_json = {}
urls = [
  "https://github.com/keras-team/keras",
  "https://github.com/scikit-learn/scikit-learn",
  "https://github.com/apache/superset",
  "https://github.com/microsoft/ML-For-Beginners",
  "https://github.com/pandas-dev/pandas",
  "https://github.com/GokuMohandas/Made-With-ML",
  "https://github.com/explosion/spaCy",
  "https://github.com/donnemartin/data-science-ipython-notebooks",
  "https://github.com/AMAI-GmbH/AI-Expert-Roadmap",
  "https://github.com/ray-project/ray",
  "https://github.com/eugeneyan/applied-ml", # parse 실
  "https://github.com/eriklindernoren/ML-From-Scratch",
  "https://github.com/streamlit/streamlit",
  "https://github.com/Lightning-AI/lightning",
  "https://github.com/academic/awesome-datascience",
  "https://github.com/plotly/dash",
  "https://github.com/fastai/fastbook",
  "https://github.com/microsoft/Data-Science-For-Beginners",
  "https://github.com/matplotlib/matplotlib"
]

# yejin: id와 repo_name을 넣으면 파싱된 결과를 리턴해줌
def whole_func(repo_urls, headers):
    for repo_url in repo_urls:
      url_dict = {"login": repo_url.split("/")[3], "repo_name": repo_url.split("/")[4]}
      topics = get_repository_infos(url_dict["login"], url_dict["repo_name"], headers)
      get_repository_README(url_dict["login"], url_dict["repo_name"], topics)
      with open('READMEs.json', 'w', encoding='utf-8') as make_file:
          json.dump(my_json, make_file, indent="\t")

def get_repository_infos(login, repo_name, headers):
    base_url = f"https://api.github.com/repos/{login}/{repo_name}"
    print(base_url)
    res = requests.get(base_url, headers=headers)
    res.raise_for_status()

    data = res.json()
    # print(data["topics"])
    return data["topics"]

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
        my_json[" ".join(topics)] = body

    elif test_r2.status_code == 200:
      print(r2)
      with urllib.request.urlopen(r2) as f:
        body = f.read().decode('utf-8')
        my_json[" ".join(topics)] = body
    else:
      print("parse 실패")
whole_func(urls, headers)     
