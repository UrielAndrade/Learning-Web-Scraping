import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://127.0.0.1:5500/index.html'

request = requests.get(url=url)

df = request.text
print(df)



