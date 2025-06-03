import pandas as pd # Importa a biblioteca pyautogui para automação de tarefas
import time # Importa a biblioteca pandas para manipulação de dados
import pyautogui # Importa a biblioteca pyautogui para automação de teclado e mouse

time.sleep(5)  # Pausa a execução por 3 segundos para garantir que o ambiente esteja pronto
print(pyautogui.position())  # Imprime a posição atual do mouse


tabela = pd.read_csv("produtos.csv")
print(tabela)
