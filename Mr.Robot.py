import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

df = pd.read_excel('') # Insira o caminho do aquivo aqui

chrome = webdriver.Chrome()
url = '' #insira sua url aqui

chrome.get(url)

time.sleep(35)

for index, row in df.iterrows():
    try:
        elemento = chrome.find_element(By.XPATH, '') #insira o XPATH aqui
        elemento.clear()
        elemento.send_keys(row['Nome da coluna'])
    except Exception as e:
        print(f"Erro ao encontrar o elemento pelo XPath: {e}")
        continue

    time.sleep(1)

chrome.quit()

input('Pressione qualquer tecla para sair')
