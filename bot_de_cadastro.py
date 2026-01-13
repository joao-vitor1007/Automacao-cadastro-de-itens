
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press("win")
time.sleep(2)
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(3)
 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)



pyautogui.click(x=840, y=360)

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") 
pyautogui.write("sua senha")
pyautogui.click(x=974, y=523)
time.sleep(3)



tabela = pd.read_csv("produtos.csv")

print(tabela)
  


for linha in tabela.index:
    
    pyautogui.click(x=840, y=238)
    25.0
    
    pyautogui.  write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)
    