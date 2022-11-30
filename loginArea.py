from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://admin.payfi.ng/")
    driver.maximize_window()
    driver.implicitly_wait(50)
    action = ActionChains(driver)
    driver.find_element(By.NAME, "email").send_keys("Olamide.john@payfi.ng")
    driver.find_element(By.NAME, "password").send_keys("Testqa1101$")
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/form/div/div[2]/div").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/form/div/div[2]/div/button").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/li[2]/a/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div["
                                  "2]/div/div/p[2]").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div["
                                  "2]/div/div/p[3]").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div["
                                  "2]/div/div/p[4]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[5]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[6]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/button/span").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/span[2]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/button/span").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/button/span").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[2]").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[3]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[2]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[3]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[4]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[5]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[6]").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[2]/a/p").click()
    driver.find_element(By.NAME, "search").click()
    driver.find_element(By.NAME, "search").send_keys("olamide.john@payfi.ng")
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div["
                                  "3]/div/div/div/div/table/tbody/tr/td[3]/p").click()
    driver.find_element(By.XPATH , "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div["
                                  "2]/a/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div["
                                  "5]/div/div/div/div/div/p[2]").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[3]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[4]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[6]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[7]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[8]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[9]/a/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[3]/a/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[4]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/p[2]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/p[3]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/p[4]").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[5]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr/td/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[6]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr/td/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[7]/a/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[8]/a/p").click()
    driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[7]/a/p").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[2]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[3]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[4]").click()
    driver.find_element(By.XPATH,
                        "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/ul/li/a/p").click()
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys("Olamide.john@payfi.ng")
    driver.find_element(By.NAME, "password").clear()


if __name__ == "__main__":
    main()
