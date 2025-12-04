import browser_cookie3
import requests
from bs4 import BeautifulSoup

matriculaSiap = "2024102020050"  
cookies = browser_cookie3.chrome(domain_name='suap.ifro.edu.br')

session = requests.Session()
session.cookies.update(cookies)

url = f"https://suap.ifro.edu.br/edu/aluno/{matriculaSiap}"
resp = session.get(url)

if resp.status_code != 200:
    print("Falha ao acessar página. Status:", resp.status_code)
    exit()

html = resp.text
soup = BeautifulSoup(html, "html.parser")

campos = {
    "Nome": "Nome",
    "Matrícula": "Matrícula",
    "E-mail Acadêmico": "E-mail Acadêmico",
    "CPF": "CPF",
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
