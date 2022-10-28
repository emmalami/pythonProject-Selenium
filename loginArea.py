from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://admin-staging.payfi.ng/")
    login = driver.find_element(By.NAME, "email").send_keys("olamide.john@outlook.com")
    password = driver.find_element(By.NAME, "password").send_keys("Testqa1101$")
    button = driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div > div > form > div > div.col-md-6.col-12.register-form-view-cover-row-form > div > button")
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        print("link", link.text)
    driver.close()


main()