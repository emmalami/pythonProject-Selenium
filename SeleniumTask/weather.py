from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    morning = driver.find_element(By.XPATH, "//span[normalize-space()='29°']")
    Afternoon = driver.find_element(By.XPATH, "//div[@class='Column--temp--5hqI_']//span["
                                              "@data-testid='TemperatureValue'][normalize-space()='34°']")
    Evening = driver.find_element(By.XPATH, "//span[normalize-space()='25°']")
    Overnight = driver.find_element(By.XPATH, "//span[normalize-space()='22°']")
    print("morning",morning.text)
    print("Afternoon",Afternoon.text)
    print("Evening",Evening.text)
    print("Overnight",Overnight.text)
    sleep(4)
    driver.close()


main()