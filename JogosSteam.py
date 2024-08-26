from constants import FTC_LOGIN, FTC_SENHA
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def main(): 
    navegador = abrirNavegador('https://store.steampowered.com/search/?filter=topsellers')
    jogos = getFilhos(getPanelById(navegador, 'search_resultsRows'))
    for jogo in jogos:
        print(jogo.text)
        print('')
        print('---------------------')
        print('')
    esperar(5)

def abrirNavegador(link):
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get(link)
    return navegador

def esperar(tempo):
    time.sleep(tempo)

def getPanelById(navegador, panelId):
    try:
        panel = navegador.find_element(By.ID, panelId)
        return panel
    except NoSuchElementException:
        print(f"Elemento com ID '{panelId}' não foi encontrado.")

def getFilhos(panel):
    return panel.find_elements(By.TAG_NAME, 'a')    

if __name__ == "__main__":
    main()