import browser_cookie3
import requests

cookies = browser_cookie3.chrome(domain_name='suap.ifro.edu.br')

session = requests.Session()
session.cookies.update(cookies)

url_matricula = "https://suap.ifro.edu.br/edu/aluno/2024102020056"
resp = session.get(url_matricula)

print("Status:", resp.status_code)
print(resp.text)  
