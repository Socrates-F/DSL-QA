import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_login_valido():
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash")))
    assert "You logged" in driver.page_source
    import time
    time.sleep(5)

def test_formulario():
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys("Carlos")
    driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys("Lira")
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.execute_script("window.scrollBy(0, 600);")
    driver.find_element(By.CSS_SELECTOR, "#submit").submit()
    WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-content")))
    assert "Thanks" in driver.page_source
    import time
    time.sleep(10)

def test_upload_arquivo():
    driver.get("https://the-internet.herokuapp.com/upload")
    driver.find_element(By.CSS_SELECTOR, "#file-upload").send_keys("../tests/upload_teste.txt")
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
    assert "File Uploaded!" in driver.page_source
    import time
    time.sleep(10)

def test_carregamento_lento():
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    WebDriverWait(driver, 15.0).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish")))
    assert "Hello World" in driver.page_source

def test_maps_localizacao():
    driver.get("https://www.google.com/maps")
    WebDriverWait(driver, 15.0).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#searchboxinput")))
    driver.find_element(By.CSS_SELECTOR, "input#searchboxinput").send_keys("Escola Politécnica de Pernambuco")
    WebDriverWait(driver, 10.0).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Pesquisar']")))
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Pesquisar']").click()
    import time
    time.sleep(10)
    WebDriverWait(driver, 15.0).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#searchboxinput")))
    assert "Recife" in driver.page_source
    import time
    time.sleep(10)

def test_github_search():
    driver.get("https://github.com/search?q=antlr+python")
    WebDriverWait(driver, 10.0).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='results-list']")))
    assert "antlr" in driver.page_source
    import time
    time.sleep(6)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Uso: python saida_selenium.py <nome_do_teste> | all')
        driver.quit()
        sys.exit()

    arg = sys.argv[1]

    if arg == 'all':
        test_login_valido()
        test_formulario()
        test_upload_arquivo()
        test_carregamento_lento()
        test_maps_localizacao()
        test_github_search()
    else:
        try:
            globals()[f'test_{arg}']()
        except KeyError:
            print(f'Teste {arg} não existe!')

    driver.quit()