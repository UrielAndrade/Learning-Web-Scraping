from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--user-data-dir=/home/uriel/.config/google-chrome")
options.add_argument("--profile-directory=Default")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=options)
driver.get("https://suap.ifro.edu.br/edu/aluno/2024102020056/")

wait = WebDriverWait(driver, 15)

ITEM = ""

elemento = wait.until(
  EC.presence_of_element_located((By.CSS_SELECTOR, ITEM ))
)
print("Resultado:", elemento.text)
input("Pressione ENTER para fechar...") 
