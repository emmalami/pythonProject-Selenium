from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


# Challenge 5
# Using any browser, navigate to any Youtube video of your choice, allow your script to wait for the comments to load
# then get the first two comments, and print them in the terminal.
def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def get_comment(driver):
    driver.get("https://www.youtube.com/watch?v=VGecJY7u6So")
    action = ActionChains(driver)
    driver.maximize_window()
    sleep(60)
    scroll_by_offset(action, 450)
    web_driver_wait = WebDriverWait(driver, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "ytd-comment-renderer")))
    comments = driver.find_elements(By.TAG_NAME, 'ytd-comment-renderer')
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content-text')
        print(comment_content.text)


def main():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    get_comment(chrome_driver)
    sleep(15)


if __name__ == '__main__':
    main()