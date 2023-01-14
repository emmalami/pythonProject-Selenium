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
        driver.get("https://www.testifyltd.com/contact")
        elements = driver.find_element(By.TAG_NAME, "h2")
        print_element_of_fields(elements)

        sleep(5)
        driver.close()

main()