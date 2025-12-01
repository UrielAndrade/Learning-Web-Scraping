from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

matriculaSiap = "2024102020056"
url = f"https://suap.ifro.edu.br/edu/aluno/{matriculaSiap}/"

options = Options()
options.add_argument("--user-data-dir=/home/uriel/.config/selenium-profile")
options.add_argument("--profile-directory=Default")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service() 

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

wait = WebDriverWait(driver, 15)

dados = [
  ("Nome", "//div[contains(@class,'list-item')][./dt[text()='Nome']]/dd"),
  ("Matricula", "//div[contains(@class,'list-item')][./dt[text()='Matrícula']]/dd",),
  ("E-mail", "//div[contains(@class,'list-item')][./dt[text()='E-mail Acadêmico']]/dd"),
  ("CPF", "//div[contains(@class,'list-item')][./dt[text()='CPF']]/dd")
  ]

for label, Xpath in dados:
  dadoBruto = wait.until(
    EC.presence_of_element_located((By.XPATH, Xpath)) # By.CSS_SELECTOR - para CSS
    )
  print(f"{label}: {dadoBruto.text}")


input("Pressione ENTER para fechar...")




# pega tudo  
# ITEM = "dl.definition-list.flex" #nao deixe vazio 

  # nome = "//div[contains(@class,'list-item')][./dt[text()='Nome']]/dd"
  # matricula = "//div[contains(@class,'list-item')][./dt[text()='Matrícula']]/dd"
  # e-mailAcademico = "//div[contains(@class,'list-item')][./dt[text()='E-mail Acadêmico']]/dd"
