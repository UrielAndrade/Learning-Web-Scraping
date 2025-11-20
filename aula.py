import requests
import pandas as pd

url = "https://coincodex.com/apps/coincodex/cache/all_coins.json"

r = requests.get(url)
coins = r.json()

df = pd.DataFrame(coins)

print(df.shape)   # mostra quantidade de moedas
print(df.head())  # primeiras linhas
