import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep


import save

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
navegador.get("https://www.sbfisica.org.br/v1/olimpiada/2022/index.php/330")

WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/main/article/ul/li[1]/a')))

cont_link = 1
controle_link = True

alunos = []

while(controle_link):
            
    try:
        ano = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/article/ul/li['+str(cont_link)+']/a').text.split(" ")

        ano_aluno = ano[1] + ' ' + ano[2]

        navegador.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/article/ul/li['+str(cont_link)+']/a').click()

        controle = True

        aux = []

        cont  = 1

        while(controle):

            try:
                aux.append(navegador.find_element(By.XPATH, '//*[@id="tm-content"]/article/table/tbody/tr['+str(cont)+']/td[1]').text)
                aux.append(navegador.find_element(By.XPATH, '//*[@id="tm-content"]/article/table/tbody/tr['+str(cont)+']/td[2]').text)
                aux.append(navegador.find_element(By.XPATH, '//*[@id="tm-content"]/article/table/tbody/tr['+str(cont)+']/td[3]').text)
                aux.append(navegador.find_element(By.XPATH, '//*[@id="tm-content"]/article/table/tbody/tr['+str(cont)+']/td[4]').text)
                aux.append(ano_aluno)

                cont = cont + 1
                alunos.append(aux)
                aux = []

            except:
                controle = False

        print(alunos)

        cont_link = cont_link + 1
        navegador.back()

    except:
        controle_link = False

print(alunos)

save.salvar(alunos)