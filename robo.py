import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def executar_robo(nome, checkin, checkout, valor, comissao):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = uc.Chrome(options=options)
    driver.get("https://app.econdos.com.br")
    time.sleep(5)

    try:
        driver.find_element(By.CSS_SELECTOR, '[data-testid="login-username-input"]').send_keys("tiagoddantas@me.com")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="login-password-input"]').send_keys("W3b12345")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="login-sign-in-button"]').click()
        time.sleep(10)

        link_elem = driver.find_element(By.CSS_SELECTOR, '[data-testid="share-link-target-link"]')
        return link_elem.get_attribute("value")
    finally:
        driver.quit()