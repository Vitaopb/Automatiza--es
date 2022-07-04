import pyautogui
import time

pyautogui.press('win')
time.sleep(3)
pyautogui.write('whats')
pyautogui.press('enter')
time.sleep(30)

pyautogui.click(x=158, y=242)
# pyautogui.click(x=213, y=165)


for i in range(100):
    pyautogui.write('Boa sorte na prova, e não esquece *EU TE AMO*')
    time.sleep(1)
    pyautogui.press('enter')

time.sleep(5)
pyautogui.write('Olá Beatriz! *Eu sou a Alexa*, Victor está dormindo e me programou para mandar essas messagens para você. Boa sorte na sua prova, pelo os meus calculos você vai simplismente arrasar. *E POR FAVOR NÃO ESQUECE, ELE TE AMA GAROTA!*')
pyautogui.press('enter')
