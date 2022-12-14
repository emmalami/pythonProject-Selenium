from telnetlib import EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://bbc.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    news1_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/a')
    print("News1 Link:", news1_link.text)
    news2_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[2]/div/a')
    print("News2 Link:", news2_link.text)
    news3_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]/div/a')
    print("News3 Link:", news3_link.text)
    news4_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]/div/a')
    print("News4 Link:", news4_link.text)
    news5_link = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]/div/a')
    print("News5 Link:", news5_link.text)
    news6_link = driver.find_element(By.XPATH,
                                     '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[2]/div/div[2]/h3/a')
    print("News6 Link:", news6_link.text)
    news7_link = driver.find_element(By.XPATH,
                                     '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[3]/div/div[2]/h3/a')
    print("News7 Link:", news7_link.text)
    news8_link = driver.find_element(By.XPATH,
                                     '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[1]/div/div[2]/h3/a')
    print("News8 Link:", news8_link.text)
    news9_link = driver.find_element(By.XPATH,
                                     '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[2]/div/div[2]/h3/a')
    print("News9 Link:", news9_link.text)
    news10_link = driver.find_element(By.XPATH,
                                      '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[3]/div/div[2]/h3/a')
    print("News10 Link:", news10_link.text)
    sleep(5)

    driver.close()


main()
