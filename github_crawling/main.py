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
token = "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" # yejin another
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
  "https://github.com/eugeneyan/applied-ml",
  "https://github.com/eriklindernoren/ML-From-Scratch",
  "https://github.com/streamlit/streamlit",
  "https://github.com/Lightning-AI/lightning",
  "https://github.com/academic/awesome-datascience",
  "https://github.com/plotly/dash",
  "https://github.com/fastai/fastbook",
  "https://github.com/microsoft/Data-Science-For-Beginners",
  "https://github.com/matplotlib/matplotlib",
  "https://github.com/binhnguyennus/awesome-scalability",
  "https://github.com/apache/spark",
  "https://github.com/ClickHouse/ClickHouse",
  "https://github.com/donnemartin/data-science-ipython-notebooks",
  "https://github.com/apache/flink",
  "https://github.com/amark/gun",
  "https://github.com/prestodb/presto",
  "https://github.com/heibaiying/BigData-Notes",
  "https://github.com/apache/predictionio",
  "https://github.com/andkret/Cookbook",
  "https://github.com/yahoo/CMAK",
  "https://github.com/questdb/questdb",
  "https://github.com/vesoft-inc/nebula",
  "https://github.com/cython/cython",
  "https://github.com/catboost/catboost",
  "https://github.com/trinodb/trino",
  "https://github.com/apache/doris",
  "https://github.com/apache/storm",
  "https://github.com/h2oai/h2o-3",
  "https://github.com/apache/beam",
  "https://github.com/scikit-learn/scikit-learn",
  "https://github.com/apache/superset",
  "https://github.com/pandas-dev/pandas",
  "https://github.com/metabase/metabase",
  "https://github.com/AMAI-GmbH/AI-Expert-Roadmap",
  "https://github.com/streamlit/streamlit",
  "https://github.com/gchq/CyberChef",
  "https://github.com/microsoft/Data-Science-For-Beginners",
  "https://github.com/allinurl/goaccess",
  "https://github.com/ml-tooling/best-of-ml-python",
  "https://github.com/gradio-app/gradio",
  "https://github.com/ydataai/pandas-profiling",
  "https://github.com/OpenRefine/OpenRefine",
  "https://github.com/airbytehq/airbyte",
  "https://github.com/Yorko/mlcourse.ai",
  "https://github.com/guipsamora/pandas_exercises",
  "https://github.com/dataease/dataease",
  "https://github.com/statsmodels/statsmodels",
  "https://github.com/yzhao062/pyod",
  "https://github.com/gonum/gonum",
  "https://github.com/eriklindernoren/ML-From-Scratch",
  "https://github.com/academic/awesome-datascience",
  "https://github.com/microsoft/LightGBM",
  "https://github.com/RaRe-Technologies/gensim",
  "https://github.com/EthicalML/awesome-production-machine-learning",
  "https://github.com/rasbt/python-machine-learning-book",
  "https://github.com/catboost/catboost",
  "https://github.com/yzhao062/anomaly-detection-resources",
  "https://github.com/yzhao062/pyod",
  "https://github.com/sktime/sktime",
  "https://github.com/jivoi/awesome-ml-for-cybersecurity",
  "https://github.com/tangyudi/Ai-Learn",
  "https://github.com/MontFerret/ferret",
  "https://github.com/rasbt/mlxtend",
  "https://github.com/biolab/orange3",
  "https://github.com/r0f1/datascience",
  "https://github.com/deanmalmgren/textract",
  "https://github.com/alibaba/Alink",
  "https://github.com/jphall663/awesome-machine-learning-interpretability",
  "https://github.com/d3/d3",
  "https://github.com/apache/echarts",
  "https://github.com/grafana/grafana",
  "https://github.com/apache/superset",
  "https://github.com/pixijs/pixijs",
  "https://github.com/metabase/metabase",
  "https://github.com/streamlit/streamlit",
  "https://github.com/academic/awesome-datascience",
  "https://github.com/directus/directus",
  "https://github.com/plotly/dash",
  "https://github.com/microsoft/Data-Science-For-Beginners",
  "https://github.com/matplotlib/matplotlib",
  "https://github.com/airbnb/visx",
  "https://github.com/plotly/plotly.js",
  "https://github.com/apexcharts/apexcharts.js",
  "https://github.com/ml-tooling/best-of-ml-python",
  "https://github.com/newTendermint/awesome-bigdata",
  "https://github.com/gradio-app/gradio",
  "https://github.com/visgl/deck.gl",
  "https://github.com/terkelg/awesome-creative-coding",
  "https://github.com/tensorflow/tensorflow",
  "https://github.com/huggingface/transformers",
  "https://github.com/pytorch/pytorch",
  "https://github.com/keras-team/keras",
  "https://github.com/scikit-learn/scikit-learn",
  "https://github.com/tesseract-ocr/tesseract",
  "https://github.com/ageitgey/face_recognition",
  "https://github.com/microsoft/ML-For-Beginners",
  "https://github.com/deepfakes/faceswap",
  "https://github.com/aymericdamien/TensorFlow-Examples",
  "https://github.com/binhnguyennus/awesome-scalability",
  "https://github.com/JuliaLang/julia",
  "https://github.com/Avik-Jain/100-Days-Of-ML-Code",
  "https://github.com/d2l-ai/d2l-zh",
  "https://github.com/iperov/DeepFaceLab",
  "https://github.com/BVLC/caffe",
  "https://github.com/ultralytics/yolov5",
  "https://github.com/GokuMohandas/Made-With-ML",
  "https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes",
  "https://github.com/tensorflow/tensorflow",
  "https://github.com/deepfakes/faceswap",
  "https://github.com/iperov/DeepFaceLab",
  "https://github.com/terryum/awesome-deep-learning-papers",
  "https://github.com/AlexeyAB/darknet",
  "https://github.com/HarisIqbal88/PlotNeuralNet",
  "https://github.com/spmallick/learnopencv",
  "https://github.com/microsoft/CNTK",
  "https://github.com/onnx/onnx",
  "https://github.com/ujjwalkarn/Machine-Learning-Tutorials",
  "https://github.com/tonybeltramelli/pix2code",
  "https://github.com/hoya012/deep_learning_object_detection",
  "https://github.com/kmario23/deep-learning-drizzle",
  "https://github.com/alexjc/neural-doodle",
  "https://github.com/ritchieng/the-incredible-pytorch",
  "https://github.com/tensorflow/tfjs-core",
  "https://github.com/facebookarchive/caffe2",
  "https://github.com/alibaba/MNN",
  "https://github.com/thtrieu/darkflow",
  "https://github.com/NVIDIA/pix2pixHD",
  "https://github.com/tensorflow/tensorflow",
  "https://github.com/huggingface/transformers",
  "https://github.com/opencv/opencv",
  "https://github.com/pytorch/pytorch",
  "https://github.com/keras-team/keras",
  "https://github.com/deepfakes/faceswap",
  "https://github.com/aymericdamien/TensorFlow-Examples",
  "https://github.com/Avik-Jain/100-Days-Of-ML-Code",
  "https://github.com/CorentinJ/Real-Time-Voice-Cloning",
  "https://github.com/d2l-ai/d2l-zh",
  "https://github.com/iperov/DeepFaceLab",
  "https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap",
  "https://github.com/BVLC/caffe",
  "https://github.com/ultralytics/yolov5",
  "https://github.com/GokuMohandas/Made-With-ML",
  "https://github.com/naptha/tesseract.js",
  "https://github.com/ZuzooVn/machine-learning-for-software-engineers",
  "https://github.com/CMU-Perceptual-Computing-Lab/openpose",
  "https://github.com/yunjey/pytorch-tutorial",
  "https://github.com/babysor/MockingBird",
  "https://github.com/tensorflow/tensorflow",
  "https://github.com/microsoft/ML-For-Beginners",
  "https://github.com/ultralytics/yolov5",
  "https://github.com/ageron/handson-ml",
  "https://github.com/lutzroeder/netron",
  "https://github.com/onnx/onnx",
  "https://github.com/mlflow/mlflow",
  "https://github.com/kubeflow/kubeflow",
  "https://github.com/ml-tooling/best-of-ml-python",
  "https://github.com/mindsdb/mindsdb",
  "https://github.com/google/dopamine",
  "https://github.com/ultralytics/yolov3",
  "https://github.com/visenger/awesome-mlops",
  "https://github.com/ludwig-ai/ludwig",
  "https://github.com/facebookarchive/caffe2",
  "https://github.com/dotnet/machinelearning",
  "https://github.com/alibaba/MNN",
  "https://github.com/pycaret/pycaret",
  "https://github.com/Netflix/metaflow",
  "https://github.com/tensorflow/serving",
  "https://github.com/scikit-learn/scikit-learn",
  "https://github.com/umami-software/umami",
  "https://github.com/qax-os/excelize",
  "https://github.com/virgili0/Virgilio",
  "https://github.com/plausible/analytics",
  "https://github.com/ydataai/pandas-profiling",
  "https://github.com/statsmodels/statsmodels",
  "https://github.com/XAMPPRocky/tokei",
  "https://github.com/gonum/gonum",
  "https://github.com/scikit-learn-contrib/imbalanced-learn",
  "https://github.com/IonicaBizau/git-stats",
  "https://github.com/mahmoud/boltons",
  "https://github.com/johnkerl/miller",
  "https://github.com/haifengl/smile",
  "https://github.com/arzzen/git-quick-stats",
  "https://github.com/blei-lab/edward",
  "https://github.com/Tautulli/Tautulli",
  "https://github.com/accord-net/framework",
  "https://github.com/boyter/scc",
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
