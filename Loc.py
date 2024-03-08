from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
import pandas as pd

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get('https://digital.detran.am.gov.br/')
wait = WebDriverWait(browser, 10)

#elementos
locadora = 'C:/Users/filho/PycharmProjects/Detran_loc/LOCADORA_2024.xlsx'
locadora_df = pd.read_excel(locadora)
renavam = str(locadora_df.loc[3,'Renavam'])[:-2]

#Clicar em veiculos
browser.find_element('xpath','//*[@id="main"]/div[1]/div/div[2]/div[3]/a/span[1]').click()

#Clicar em licenciamento
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="veiculosMenuCollapse"]/div/ul/li[1]/a'))).click()

#captcher: Primeira etapa, o renavam
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="detranDigitalModal"]/div/div/form/div[1]/div/div[2]/div[1]/input'))).send_keys(renavam)

#captcher

#clicar em cancelar protocolo
sleep(15)
try:
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="Cancelar Protocolo DETRAN-AM"]'))).click()
    print('Cancelar P')
except:
    print('não achei cancelar P')

#clicar em solicitar:
sleep(3)
try:
    solicitar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div/div[2]/div/button')))
    solicitar.click()
except Exception as e:
    print('Solcitar Problema:')
    print(e)

#pagar
sleep(3)
try:
    pagar = wait.until(EC.element_to_be_clickable((
        By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/div[3]/div/table/tr[1]/td[2]/button[1]')))
    pagar.click()
    print('Achei')
except Exception as e:
    print(e)
sleep(10)