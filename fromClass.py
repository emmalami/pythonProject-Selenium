from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://admin-staging.payfi.ng/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    login = driver.find_element(By.NAME, "email").send_keys("olamide.john@outlook.com")
    password = driver.find_element(By.NAME, "password").send_keys("Testqa1101$")
    button = driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div > div > form > div > "
                                                  "div.col-md-6.col-12.register-form-view-cover-row-form > div > "
                                                  "button").click()
    customermenu = driver.find_element(By.XPATH, "(//p[contains(@class,'nav-p')][normalize-space()='Customers'])[1]").click()
    sleep(30)
    driver.close()


main()