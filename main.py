import pyautogui
import time 

pyautogui.PAUSE = 1

# Abrir o navegador chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Acessar o site
pyautogui.write('hashtagtreinamentos.com/curso-python')
pyautogui.press('enter')

time.sleep(2)

# Preencher o formulário
pyautogui.click(x=288, y=668)
pyautogui.write('exemplo@gmail.com')


pyautogui.press('tab')
pyautogui.write('exemplo@gmail.com')

pyautogui.press('tab')
pyautogui.write('(00) 00000-0000')

# Enviar o formulário
pyautogui.press('tab')
pyautogui.press('enter')