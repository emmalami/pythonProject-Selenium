from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://payfi-testing-staging.s3-website-eu-west-1.amazonaws.com/")
    AmountField = driver.find_element(By.NAME, "amount").send_keys(30000)
    PaywithPayfi = driver.find_element(By.CSS_SELECTOR, "#root > div > div > form > div:nth-child(2) > button").click()
    sleep(20)



main()