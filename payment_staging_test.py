from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# adding incognito mood




class StagingPayment():
    def __init__(self):
        self.login = "http://payfi-testing-staging.s3-website-eu-west-1.amazonaws.com/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(1920, 1080)
        self.action = ActionChains(self.driver)
        
        
    def __first_process(self):
        self.driver.get(self.login)

        time.sleep(5)

        self.wait = WebDriverWait(self.driver, 5)

        first_page = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body")))

        
        amount = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#amount')))

        self.action.click(on_element=amount)
        # send keys
        self.action.send_keys(self.amount_value)
        self.action.send_keys(Keys.ENTER)
        # perform the operation
        self.action.perform()
        time.sleep(15)

        framee = self.driver.find_element(By.CSS_SELECTOR, 'div[id="payfi"] ')

        time.sleep(10)
        self.__payfi_frame() # switch to payfi frame

    def __payfi_frame(self):
        button = self.driver.find_elements(By.TAG_NAME, 'object')
        for b in button:
            print(b)
        frame = self.driver.switch_to.frame(button[0])

    def __phone_number_route(self):
        
        # driver find phone number route button
        phone_number_button = self.driver.find_element(By.XPATH, "//button[@type='button'][2]")
        
        # click phone number route
        self.driver.execute_script("arguments[0].click();", phone_number_button)
        time.sleep(5)

        phone_number_element = self.driver.find_element(By.XPATH, "//div[@class='input__container']//input[@type='number' and @name='phone']")
        
        # send keys user phone number
        self.action.click(on_element=phone_number_element)
        self.action.send_keys(self.phone_number)
        self.action.perform()

        drop_down = self.driver.find_element(By.XPATH, "//div[@class='dropdown-container__selected']")
        self.driver.execute_script("arguments[0].click();", drop_down)
        time.sleep(1)

        if self.invest_yield_route:
            select_payfi = self.driver.find_element(By.XPATH, "//div[@class='dropdown-content']//span[1]")
            self.driver.execute_script("arguments[0].click();", select_payfi)
            time.sleep(1)
        elif self.payfi_route:
            select_payfi = self.driver.find_element(By.XPATH, "//div[@class='dropdown-content']//span[2]")
            self.driver.execute_script("arguments[0].click();", select_payfi)
            time.sleep(1)

        continue_button = self.driver.find_element(By.XPATH, "//button[@class='payfi-button-primary login-scrollable-button' and @type='submit']")
        self.driver.execute_script("arguments[0].click();", continue_button) # go to next screen
        time.sleep(7)

        # input pin
        self.__input_pin()


    def __input_pin(self):
        pin_input_tags = self.driver.find_elements(By.TAG_NAME, 'input')

        #action.send_keys(user_phone)
        #action.perform()
        pin = self.user_pin # '3535'
        for pin_digit,tag in zip(pin, pin_input_tags):
            self.action.click(on_element=tag)
            self.action.send_keys(pin_digit)
            self.action.perform()
            time.sleep(1)
        self.__click_continue_button()
    
    def __click_continue_button(self):
        continue_button= self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][1]")))
        #self.driver.find_element(By.XPATH, "//button[@type='button'][1]")
        self.driver.execute_script("arguments[0].click();", continue_button)
        time.sleep(5)

    def __select_payment(self):
        payment_options = self.driver.find_elements(By.XPATH, "//div[@class='card-select-body']//span")
        
        if self.one_time_payment:
            self.driver.execute_script("arguments[0].click();", payment_options[0]) # One time payment button
            time.sleep(1)
            
            self.__click_continue_button() # go to "pay today" screen
            time.sleep(5)

        elif self.installment_payment:
            self.driver.execute_script("arguments[0].click();", payment_options[1]) # Pay in Installments button
            time.sleep(1)

            self.__click_continue_button() # go to "eligibility checked" screen
            self.__click_continue_button() # go to "select payment plan" screen

            # select payment plan
            select_paymnet = self.driver.find_element(By.XPATH, f"//*[contains(text(),'{self.payment_plan}')]")
            self.driver.execute_script("arguments[0].click();", select_paymnet) # Pay in Installments button
            time.sleep(5)

        
        self.__click_continue_button() # go to "review purchase" screen
        self.__click_continue_button() # go to "Enter transaction pin" screen
        
        # input pin
        self.__input_pin()

        # select debit card payment
        self.__select_card() # appears at pay now screen

    

    def __select_card(self):
        select_card = self.driver.find_elements(By.XPATH, "//div[@class='card-select-body']")
        self.driver.execute_script("arguments[0].click();", select_card[1]) # click debit card button
        time.sleep(5)

        self.__click_continue_button() # go to "pay now" screen

        self.__click_continue_button() # OPEN PAY WITH CARD WIDGET

        time.sleep(10)
        paystack_widget = self.driver.find_elements(By.TAG_NAME, 'iframe')
        for i in paystack_widget:
            print("paystack widget")
            print(i)
        
        frame = self.driver.switch_to.frame(paystack_widget[-1])

        #select_success = self.driver.find_elements(By.XPATH, "//div[@class='card']")[0]
        select_success = self.driver.find_element(By.XPATH, "//*[contains(text(),'Success')]")
        self.driver.execute_script("arguments[0].click();", select_success) # click success in paystack widget
        time.sleep(5)

        pay_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][1]")
        self.driver.execute_script("arguments[0].click();", pay_button)
        time.sleep(17)
        
        # switch to payfi frame
        self.driver.switch_to.parent_frame()
        
        self.__click_continue_button() # final "Okay" button
        time.sleep(3)

    def run(self, amount_value, phone_number, user_pin, one_time_payment=True, installment_payment=False, payment_plan='2'):
        self.amount_value = amount_value # '60000'
        self.phone_number = phone_number # '08067935224'
        self.invest_yield_route = False
        self.payfi_route = True
        self.user_pin = user_pin # '3535'
        self.one_time_payment = one_time_payment # True or False
        self.installment_payment = installment_payment # True or False
        self.payment_plan = payment_plan # '2' or '3' or '4' or '5' or '6'

        # run first process
        self.__first_process()

        # phone number route
        self.__phone_number_route()

        # select payment type [one time payment or installment payment] -- both can't be both True|True or False|False
        self.__select_payment()




staging_payment = StagingPayment()

staging_payment.run(
    amount_value="30000", phone_number="08067935224", user_pin="3535",
    one_time_payment=True, installment_payment=False, payment_plan='2')





