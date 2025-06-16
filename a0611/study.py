import requests
from bs4 import beautifulsoup
url = "https://news.ycombinator.comjh/"
res = requests.get(url)


print(res.status_code)