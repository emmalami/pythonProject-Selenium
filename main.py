from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import EdgeDriver


def main():
    driver = webdriver.Edge(executable_path='C:\\Users\\Dogit init
    driver = webdriver.Edge(service=Service(EdgeDriver().install()))
    driver.get("https://www.google.com")
    driver.close()


main()
