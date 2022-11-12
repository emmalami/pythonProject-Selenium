from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(" https://www.bbc.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    # print(driver.find_element(By.XPATH,"/html/body").text)   #to print out content of an entire page
    # Getting all sections from BBC
    media_list = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "section"))

        for item in media_list:
    print(item.find_element(By.CSS_SELECTOR, 'trying to figure what to write here')

    sleep(4)
    driver.close()


main()