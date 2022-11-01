from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://admin-staging.payfi.ng/")
    login = driver.find_element(By.NAME, "email").send_keys("olamide.john@outlook.com")
    password = driver.find_element(By.NAME, "password").send_keys("Testqa1101$")
    button = driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div > div > form > div > "
                                                  "div.col-md-6.col-12.register-form-view-cover-row-form > div > "
                                                  "button").click()
    findXpath = driver.find_element(By.XPATH, "//form[1]")
    print(findXpath)
    sleep(30)

    # links = driver.find_elements(By.TAG_NAME, "a")
    # print("link", links)
    driver.close()


main()
