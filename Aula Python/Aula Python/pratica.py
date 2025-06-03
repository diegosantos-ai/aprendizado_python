import pyautogui # Importa a biblioteca pyautogui para automação de teclado e mouse
import time # Importa a biblioteca pyautogui para automação de teclado e mouse

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> apertar 1 tecla
# pyautogui.press -> escrever um texto
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3  # define um tempo de pausa entre os comandos, para evitar que o programa execute muito rápido    

# chamar pyautogui sempre no começo do código

# Regra de Ouro: sempre fazer o passo a passo da logica do programa para poder fazer o código, depois iniciar a codificação

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # abrir o navegador (chrome)
pyautogui.press("win")  # abre o menu iniciar
pyautogui.write("chrome")  # escreve "chrome"
pyautogui.press("enter")  # pressiona "enter" para abrir o navegador
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # escreve o link
pyautogui.press("enter")  # pressiona "enter" para acessar o link

# espera 3 segundos para a página carregar
pyautogui.sleep(3)  # aguarda 3 segundos para a página carregar

# Passo 2: Fazer Login
pyautogui.click(x=-1401, y=510)  # clica no campo de email
pyautogui.write("santos.diegoj86@gmail.com")  # escreve o email
pyautogui.press("tab")  # passa para o próximo campo
pyautogui.write("SenhasenhasenhaS")  # escreve a senha
pyautogui.press("tab")  # passa para o próximo campo
pyautogui.press("enter")  # pressiona "enter" para fazer login
time.sleep(3)  # espera 3 segundos para o login ser processado

# Passo 3: Importar a base de dados
import pandas # Importa a biblioteca pandas para manipulação de dados

tabela = pandas.read_csv("produtos.csv")  # lê o arquivo CSV com os dados dos produtos
print(tabela)  # imprime a tabela no console

# Passo 4: Cadastrar 1 produto

pyautogui.click(x=-1485, y=370)  # clica no campo de código

codigo =  "MOLO000251"  # define o código do produto
pyautogui.write(codigo)  # escreve o código do produto
pyautogui.press("tab")  # passa para o próximo campo
marca = "Logitech"  # define a marca do produto
pyautogui.write(marca)  # escreve a marca do produto
pyautogui.press("tab")  #passa para o próximo campo
tipo = "Mouse"  # define o tipo do produto
pyautogui.write(tipo)  # escreve o tipo do produto
pyautogui.press("tab")  # passa para o próximo campo
categoria = "1"  # define a categoria do produto
pyautogui.write(categoria)  # escreve a categoria do produto
pyautogui.press("tab")  # pass5 a para o próximo campo
preco_unitario = "25.95"  # define o preço unitário do produto
pyautogui.write(preco_unitario)  # escreve o preço unitário do produto
pyautogui.press("tab")  # passa para o próximo campo
custo = "6.5" # define o custo do produto
pyautogui.write(custo)  # escreve o custo do produto
pyautogui.press("tab")  # passa para o próximo campo

obs = ""

# Repetir o passo 4 para todos os produtos da base de dados

##### essa é a lógica de programação.

# Agora é se perguntar: como eu faço cada passo no Python?

# pyautogui é uma biblioteca que simula o teclado e mouse do computador, permitindo automatizar tarefas repetitivas.
# Faz Automaões com Python

#########################################################################################################################

