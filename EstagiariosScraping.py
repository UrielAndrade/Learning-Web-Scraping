from bs4 import BeautifulSoup
import csv
from datetime import datetime

arquivo_html = "Estágios - SUAP_ Sistema Unificado de Administração Pública.html"

with open(arquivo_html, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

tabelas = soup.find_all("table")
print(f"Total de tabelas encontradas: {len(tabelas)}")

for i, tb in enumerate(tabelas, 1):
    print(f"{i}: classes = {tb.get('class')}")

# procurar td -> field-aluno
tabela = None
for tb in soup.find_all("table"):
    if tb.find("td", {"class": "field-aluno"}):
        tabela = tb
        break

if not tabela:
    print("Tabela not found.")
    exit()


estagios = []
linhas = tabela.find_all("tr")
campos_td = {
    "Aluno": "field-aluno",
    "Empresa": "field-empresa",
    "Orientador": "field-orientador",
    "Data Início": "field-data_inicio",
    "Data Prevista Fim": "field-data_prevista_fim",
    "Data Fim": "field-data_fim",
    "Campus": "field-get_campus",
}

for tr in linhas:
    estagio = {}
    valido = True

    for label, classe in campos_td.items():
        td = tr.find("td", {"class": classe})
        if not td:
            valido = False
            break
        estagio[label] = td.get_text(strip=True)

    if valido:
        estagios.append(estagio)

# Mostrar
for i, estagio in enumerate(estagios, 1):
    print(f"\n--- ESTÁGIO {i} ---")
    for k, v in estagio.items():
        print(f"{k}: {v}")

# Exportar CSV
nome_arquivo = f"estagios_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.csv"
with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=campos_td.keys())
    writer.writeheader()
    writer.writerows(estagios)

print(f"\n✓ Exportado: {nome_arquivo}")
print(f"✓ Total encontrados: {len(estagios)}")
