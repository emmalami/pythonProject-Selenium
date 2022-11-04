from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def print_element_of_fields(element):
    print("Text", element.text)
    print("Size", element.size)
    print("Tag name", element.tag_name)
    print("Location", element.location)
    print("Accessible Name", element.accessible_name)
    print("Aria Role", element.aria_role)
    print("ID", element.id )
    print("Rectangle", element.rect)



def main():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://admin-staging.payfi.ng/")
        login = driver.find_element(By.NAME, "email").send_keys("olamide.john@payfi.ng")
        password = driver.find_element(By.NAME, "password").send_keys("Testqa1101$")
        element = driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div > div > form > div > "
                                                      "div.col-md-6.col-12.register-form-view-cover-row-form > div > "
                                                      "button").click()
        sleep(30)
        driver.close()

main()