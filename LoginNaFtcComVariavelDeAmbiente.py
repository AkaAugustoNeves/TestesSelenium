from constants import FTC_LOGIN, FTC_SENHA
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def main(): 
    navegador = abrirNavegador('https://aluno.uniftc.edu.br/#/login')
    setValueInput(getInputPorId(navegador, 'login'), FTC_LOGIN)
    setValueInput(getInputPorId(navegador, 'senha'), FTC_SENHA)
    enviarFormulario(getButtonSubmit(navegador))
    esperar(5)

def abrirNavegador(link):
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get(link)
    return navegador

def esperar(tempo):
    time.sleep(tempo)

def getInputPorId(navegador, inputId):
    try:
        input = navegador.find_element(By.ID, inputId)
        return input
    except NoSuchElementException:
        print(f"Elemento com ID '{inputId}' não foi encontrado.")

def setValueInput(input, value):
    input.send_keys(value)

def getButtonSubmit(navegador):
    return navegador.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

def enviarFormulario(botao):
    botao.click()
    


if __name__ == "__main__":
    main()