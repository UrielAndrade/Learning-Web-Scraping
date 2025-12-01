from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.binary_location = "/usr/sbin/google-chrome-stable"

# perfil isolado (o Chrome NAO vai fechar)
options.add_argument("--user-data-dir=/tmp/selenium-profile")
options.add_argument("--profile-directory=Default")

# flags do linux
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

input("Pressione ENTER para fechar...")
