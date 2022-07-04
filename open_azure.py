import os
import time
import pyautogui
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from traitlets import default

load_dotenv()


class azure():
    def __init__(self):
        self.drive = webdriver.Chrome()
        self.email = os.environ['email']
        self.password = os.environ["password"]

    def acessar_azure(self):
        drive = self.drive
        drive.get(os.environ["url_azure"])
        time.sleep(2)
        
        email = drive.find_element_by_xpath('//*[@id="i0116"]')
        email.send_keys(self.email)
        email.send_keys(Keys.ENTER)

        time.sleep(2)

        password = drive.find_element_by_id("i0118")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

        yes_btn = drive.find_element_by_xpath('//*[@id="idSIButton9"]')
        yes_btn.send_keys(Keys.ENTER)

        
        
    def abrir_pull_request(self, repository, branch):
        drive = self.drive

        match repository:
          case "keener":
            keener_project = drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[3]/td/div')
            webdriver.ActionChains(drive).double_click(keener_project).perform()
            time.sleep(2)
            

    def digitar_msg_discord(task_name):
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write("discord")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=24, y=409)
        time.sleep(1)
        pyautogui.write(task_name)
        time.sleep(1)
        pyautogui.keyDown("shift")
        pyautogui.press("enter")
        pyautogui.keyUp("shift")
        
repos = ["keener site", "case", "globus", "labet"]


print("Repositórios:")
for i in repos:
  print(i)
repository = input("Digite o nome do repositório: ")
task_name = input("Digite o nome da tarefa: ")


startAzure = azure()
startAzure.acessar_azure()
startAzure.abrir_pull_request(repository.lower())

