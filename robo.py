from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
def download_Dae(placa, renavam):
    # Instanciando o driver
    driver = webdriver.Chrome()

    # URL que eu vou entrar
    driver.get("http://www2.sefaz.ce.gov.br/ipva/#/impostos/emitir-dae")

    sleep(2)

    # Achando o local para colocar a placa
    placa_area = driver.find_element(by=By.ID, value="md-input-3")
    placa_area.send_keys(placa)

    # Achando o local para colocar o renavam
    renavam_area = driver.find_element(by=By.ID, value="md-input-5")
    renavam_area.send_keys(renavam)

    # Utilizando XPath para encontrar o botão de pesquisa
    btn_psq = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div/ngc-sidenav/div/div[3]/app-emitir-dae/div/div/md-card/div/form/div[1]/div[4]/button[1]")
    btn_psq.click()

    sleep(2)

    # Achando o botão de download dae e clicando nele
    btn_download_dae = driver.find_element(by=By.ID, value="dae-cota-unica")
    btn_download_dae.click()

    sleep(2)

    # Achando o botão de imprimir dae e clicando nele
    btn_imprimir_dae = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div/ngc-sidenav/div/div[3]/app-emitir-dae/div/div/md-card/div[4]/form/fieldset/div/div[2]/div/button[1]")
    btn_imprimir_dae.click()    
    sleep(5)
    
    pyautogui.hotkey('ctrl', 's')
    sleep(2)
    pyautogui.typewrite(f"{placa}")
    sleep(2)
    pyautogui.press('enter')
    sleep(2)  # Ajuste conforme necessário

    driver.quit()
