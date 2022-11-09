from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    googleword = driver.find_element(By.NAME, "q").send_keys("python")
    button = driver.find_element(By.NAME, "btnK").click()
    result = driver.find_element(By.XPATH, "//div[@class='SPZz6b']")
    print(result.text)
    sleep(5)
    driver.close()



main()