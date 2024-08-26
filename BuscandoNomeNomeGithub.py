from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#Abrindo navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://github.com/AkaAugustoNeves')
# navegador.maximize_window()
time.sleep(5)

# main = navegador.find_element(By.XPATH,'/html/body/div/div[4]/main/div/div/div/div')
card = navegador.find_element(By.CLASS_NAME,'vcard-names-container')
nome = card.find_element(By.XPATH, './/h1/span')
print(nome.text)
time.sleep(10)