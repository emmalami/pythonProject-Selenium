from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    email = driver.find_element(By.NAME, "email").send_keys("olamide.john@outlook.com")
    password = driver.find_element(By.NAME, "pass").send_keys("0$aMIDEJOHN1101")
    loginbutton = driver.find_element(By.NAME, "login").click()
    sleep(30)
    driver.close()


main()