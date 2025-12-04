from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

URL_BASE = "https://suap.ifro.edu.br"

options = Options()
options.add_argument("--user-data-dir=/home/uriel/.config/selenium-cookie-capture")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print("➡ Abra o SUAP e faça login manualmente...")
driver.get(URL_BASE)
input("✔ Depois de logado, aperte ENTER... ")

print("➡ Capturando cookies...")

cookies = driver.get_cookies()

# Filtra apenas cookies do domínio correto
valid = []
for c in cookies:
    if c.get("domain") in ["suap.ifro.edu.br", ".suap.ifro.edu.br"]:
        valid.append({
            "name": c["name"],
            "value": c["value"],
            "domain": "suap.ifro.edu.br",
            "path": c.get("path", "/")
        })

with open("cookies_suap.json", "w") as f:
    json.dump(valid, f, indent=2)

print("✔ Cookies salvos com sucesso!")
input("ENTER para fechar...")
driver.quit()
