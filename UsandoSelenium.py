from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.coingecko.com/pt')
driver.implicitly_wait(5)

