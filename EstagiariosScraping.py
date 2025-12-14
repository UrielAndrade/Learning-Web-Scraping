import browser_cookie3
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import requests
import browser_cookie3
import requests

# nao precisa para esta página
matriculaSiap = ""
cookies = browser_cookie3.chrome(domain_name='suap.ifro.edu.br')

session = requests.Session()
session.cookies.update(cookies)

url = f"https://suap.ifro.edu.br/admin/estagios/praticaprofissional/?aluno__situacao=1"
response = session.get(url)

pageStatusCode = response.status_code
if pageStatusCode != 200:
    print("flaha, Status:", pageStatusCode)
    exit()

html = response.text
soup = BeautifulSoup(html, "html.parser")

estagiarios = []
campos = {
    "Aluno": "field-aluno",
    "Empresa": "field-empresa",
    "Orientador": "field-orientador",
    "Data Início": "field-data_inicio",
    "Data Prevista Fim": "field-data_prevista_fim",
    "Data Fim": "field-data_fim",
    "Campus": "field-get_campus",
}

resultado = {}

for label, texto_procurado in campos.items():
    dt = soup.find("dt", string=lambda s: s and texto_procurado in s)
    if dt:
        dd = dt.find_next("dd")
        if dd:
            resultado[label] = dd.get_text(strip=True)
        else:
            resultado[label] = None
    else:
        resultado[label] = None

for k, v in resultado.items():
    print(f"{k}: {v}")
