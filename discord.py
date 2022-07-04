import pyautogui
import time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("discord")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=24, y=409)
time.sleep(5)

print(pyautogui.position())