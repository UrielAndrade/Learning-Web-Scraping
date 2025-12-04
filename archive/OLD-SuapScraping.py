import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

matriculaSiap = "2024102020056"
url = f"https://suap.ifro.edu.br/edu/aluno/{matriculaSiap}/"

# =======================
# CARREGAR COOKIES
# =======================
with open("cookies_suap.json", "r") as f:
    cookies = json.load(f)

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(), options=options)

# Primeiro abre o domínio para poder inserir cookies
driver.get("https://suap.ifro.edu.br/")
time.sleep(2)

# =======================
# INJETAR COOKIES
# =======================
for cookie in cookies:
    cookie.pop("sameSite", None)        # Selenium não aceita
    cookie.pop("expirationDate", None)  # Pode dar erro
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(2)  # garante que o login foi aplicado

# =======================
# AGORA ACESSA A PÁGINA DO ALUNO JÁ LOGADO
# =======================
driver.get(url)
wait = WebDriverWait(driver, 15)

dados = [
    ("Nome", "//div[contains(@class,'list-item')][./dt[text()='Nome']]/dd"),
    ("Matrícula", "//div[contains(@class,'list-item')][./dt[text()='Matrícula']]/dd"),
    ("E-mail Acadêmico", "//div[contains(@class,'list-item')][./dt[text()='E-mail Acadêmico']]/dd"),
    ("CPF", "//div[contains(@class,'list-item')][./dt[text()='CPF']]/dd"),
]

print("\n=== DADOS DO ALUNO ===\n")

for label, xpath in dados:
    try:
        el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        print(f"{label}: {el.text}")
    except:
        print(f"{label}: não encontrado")

input("\nPressione ENTER para fechar...")
