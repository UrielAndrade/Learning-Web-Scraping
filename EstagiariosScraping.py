import browser_cookie3
from bs4 import BeautifulSoup
import requests

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

tabela = soup.find("table", class_="results")
if not tabela:
    print("Tabela não encontrada")
    exit()

def texto(linha, classe):
    td = linha.find("td", class_=classe)
    return td.get_text(strip=True) if td else None

estagiarios = []
for linha in tabela.select("tbody tr"):
    estagiarios.append({
        "Aluno": texto(linha, "field-aluno"),
        "Empresa": texto(linha, "field-empresa"),
        "Orientador": texto(linha, "field-orientador"),
        "Data Início": texto(linha, "field-data_inicio"),
        "Data Prevista Fim": texto(linha, "field-data_prevista_fim"),
        "Data Fim": texto(linha, "field-data_fim"),
        "Campus": texto(linha, "field-get_campus"),
    })
    print(len(estagiarios))
