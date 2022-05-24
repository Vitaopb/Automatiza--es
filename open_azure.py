import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()


class azure():
    def __init__(self):
        self.drive = webdriver.Chrome()
        self.email = os.environ['email']
        self.password = os.environ["password"]
        print(self.email, self.password)

    def acessar_azure(self):
        drive = self.drive
        drive.get("https://dev.azure.com/KeenerIo")
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

        keener_project = drive.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/table/tbody/tr[3]/td/div')
        webdriver.ActionChains(drive).double_click(keener_project).perform()
        time.sleep(2)
        
    def abrir_pull_request(self, repository, branch):
        drive = self.drive
        print(repository)
        print(branch)


print("Vai abrir uma pull request? (s/n)")
abrir_pull_requets = input("Digite: " )

if (abrir_pull_requets == "s"):
  repository = input("Digite o nome do repositório: ")
  branch = input("Digite o nome da branch: ")
  startAzure = azure()
  startAzure.acessar_azure()
  startAzure.abrir_pull_request(repository, branch)
else:
  startAzure = azure()
  startAzure.acessar_azure()

