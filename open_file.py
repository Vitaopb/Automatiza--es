import pyautogui
import time

pyautogui.press('win')
pyautogui.write('cmd')

pyautogui.press('enter')

time.sleep(1.4)

pyautogui.write("cd Documents\projects\pyauto && python add_hours_portal.py")
# pyautogui.write('cd Documents\projects\Automatizações && python add_hours_portal.py')
pyautogui.press('enter')
