import pyautogui
import time

pyautogui.alert('O codigo vai começar. nao use seu pc')
pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('winleft','d')
pyautogui.moveTo(1321,46)
pyautogui.mouseDown()
pyautogui.moveTo(417,618)
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.mouseUp()
time.sleep(8)
pyautogui.alert("o codigo acabou de rodar")
