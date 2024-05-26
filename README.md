# Preenchimento Automático de Formulário com Selenium 

>   Este repositório contém um script Python que automatiza o preenchimento de formulários em um site web usando Selenium WebDriver. O script lê dados de um arquivo Excel usando o pandas e insere esses dados em campos de formulário específicos no site.

### Requisitos
+ Python 3.6 ou superior
+ pandas
+ selenium

## Instalação

### Clone este repositório:
https://github.com/gregorygustavo80/Mr.Robot.git

### Instale as dependências necessárias:

#### pip install pandas selenium

### Uso
Prepare seu arquivo Excel com os dados que você deseja inserir no formulário. Certifique-se de que o nome da coluna no arquivo Excel corresponda ao nome da coluna usado no script.

### Insira o caminho do arquivo Excel aqui
df = pd.read_excel('caminho/do/arquivo.xlsx')

### Insira sua URL aqui
url = 'https://www.example.com'

### Aguarde o site carregar completamente (ajuste o tempo conforme necessário)
time.sleep(35)

#### Adicione o XPATH e o nome da coluna do seu arquivo .xlsx
    try:
        # Insira o XPATH do campo do formulário aqui
        elemento = chrome.find_element(By.XPATH, 'seu/xpath/aqui')
        elemento.clear()
        elemento.send_keys(row['Nome da coluna'])
    except Exception as e:
        print(f"Erro ao encontrar o elemento pelo XPath: {e}")
        continue
    time.sleep(1)

## Execute o script:
python Mr.Robot.py

### Observações
Certifique-se de ajustar o tempo de espera (time.sleep) conforme necessário para garantir que o site carregue completamente antes de tentar interagir com os elementos do formulário.
Verifique os XPATHs dos campos do formulário no site que você está automatizando, pois eles podem variar.

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar este script.

### Exemplo de arquivo Excel
O arquivo Excel deve ter a seguinte estrutura:

### Nome da coluna
### Valor 1
### Valor 2
### Valor 3

>Substitua Nome da coluna pelo nome real da coluna que você usará no script.

### Para obter o XPATH de um campo do formulário:

+ Abra o site no seu navegador.
+ Clique com o botão direito no campo do formulário e selecione "Inspecionar" (ou pressione Ctrl+Shift+I).
+ Clique com o botão direito no elemento HTML do campo do formulário e selecione "Copiar" > "Copiar XPATH".
+ Certifique-se de que o XPATH copiado seja único e identifique apenas o campo desejado.
