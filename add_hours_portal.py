import os
import time
import pyautogui
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()

class add_hours_portal():
  def __init__(self):
      self.drive = webdriver.Chrome()
      self.email = os.environ['email']
      self.password = os.environ["password_portal"]
  
  def login_portal(self):
    drive = self.drive
    
    drive.get(os.environ['url_portal'])
    
    email = drive.find_element_by_xpath('//*[@id="input-31"]')
    email.send_keys(self.email)
    
    password = drive.find_element_by_xpath('//*[@id="input-35"]')
    password.send_keys(self.password)
    
    drive.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/button').click() # Click no btn logar
    
  def add_task(self, task_description, project_number, task_hours): 
    drive = self.drive
    
    time.sleep(5)
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div/nav/div[1]/div[2]/a[2]').click() # btn de terefas
    time.sleep(2)
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/div/div[3]/div[1]/div[2]/a').click() # btn de add tarefas
    
    time.sleep(2)
    
    match project_number:
      case '0':
        drive.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div/div/form/div[1]/div[1]/div/div/div[1]/div[1]').click()
        pyautogui.press("down", 30, 0.1)
        drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[25]/div').click()
      case '1':
        drive.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/main/div/div/div/div/form/div[1]/div[1]/div/div/div[1]/div[1]').click()
        pyautogui.press("down", 30, 0.1)
        drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[28]/div').click()

    drive.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/div/div/div/form/div[1]/div[3]/div/div/div/div/div').click() # Sem card
    
    drescription = drive.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/div/div/div/form/div[1]/div[4]/div/div/div/div/textarea')
    drescription.send_keys(task_description)
    
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/div/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]').click()
    
    time.sleep(1.5)
    
    horas = drive.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/div/div/div/form/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/input')
    horas.send_keys(task_hours)
    
    time.sleep(1.5)
    
    drive.find_element_by_xpath('/html/body/div[1]/div/div/div/main/div/div/div/div/div/button').click()
    
task_description = input("Digite o nome da tarefa: ")
project = input("Qual o projeto - [Keener Estudo - 0] / [Keneer Portal - 1]: ")
hours = input("Digite as horas trabalhadas: ")

portal = add_hours_portal()
portal.login_portal()
portal.add_task(task_description, project, hours)