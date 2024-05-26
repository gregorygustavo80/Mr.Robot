Preenchimento Automático de Formulário com Selenium

Este repositório contém um script Python que automatiza o preenchimento de formulários em um site web usando Selenium WebDriver. O script lê dados de um arquivo Excel e insere esses dados em campos de formulário específicos no site.

Requisitos
Python 3.6 ou superior
pandas
selenium
WebDriver do navegador (ChromeDriver, msEdgeDriver, etc.)

Instalação

Clone este repositório:
https://github.com/gregorygustavo80/Mr.Robot.git

Instale as dependências necessárias:

pip install pandas selenium
Baixe o WebDriver correspondente ao navegador que você deseja usar e adicione-o ao PATH do seu sistema. 

Uso
Prepare seu arquivo Excel com os dados que você deseja inserir no formulário. Certifique-se de que o nome da coluna no arquivo Excel corresponda ao nome da coluna usado no script.

Edite o script MR.Robot para incluir o caminho do arquivo Excel, a URL do site e o XPATH dos campos do formulário.

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Insira o caminho do arquivo Excel aqui
df = pd.read_excel('caminho/do/arquivo.xlsx')

# Insira sua URL aqui
url = 'https://www.example.com'

chrome = webdriver.Chrome()
chrome.get(url)

# Aguarde o site carregar completamente (ajuste o tempo conforme necessário)
time.sleep(35)

for index, row in df.iterrows():
    try:
        # Insira o XPATH do campo do formulário aqui
        elemento = chrome.find_element(By.XPATH, 'seu/xpath/aqui')
        elemento.clear()
        elemento.send_keys(row['Nome da coluna'])
    except Exception as e:
        print(f"Erro ao encontrar o elemento pelo XPath: {e}")
        continue

    time.sleep(1)

chrome.quit()

input('Pressione qualquer tecla para sair')

Execute o script:
python Mr.Robot.py

Observações
Certifique-se de ajustar o tempo de espera (time.sleep) conforme necessário para garantir que o site carregue completamente antes de tentar interagir com os elementos do formulário.
Verifique os XPATHs dos campos do formulário no site que você está automatizando, pois eles podem variar.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar este script.

Exemplo de arquivo Excel
O arquivo Excel deve ter a seguinte estrutura:

Nome da coluna
Valor 1
Valor 2
Valor 3
...
Substitua Nome da coluna pelo nome real da coluna que você usará no script.

Para obter o XPATH de um campo do formulário:

Abra o site no seu navegador.
Clique com o botão direito no campo do formulário e selecione "Inspecionar" (ou pressione Ctrl+Shift+I).
Clique com o botão direito no elemento HTML do campo do formulário e selecione "Copiar" > "Copiar XPATH".
Certifique-se de que o XPATH copiado seja único e identifique apenas o campo desejado.
