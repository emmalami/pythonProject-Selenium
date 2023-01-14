# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://payfi-testing-staging.s3-website-eu-west-1.amazonaws.com/")
        driver.find_element_by_id("amount").click()
        driver.find_element_by_id("amount").clear()
        driver.find_element_by_id("amount").send_keys("50000")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/button[2]").click()
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("08169400538")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//input[@value='']").click()
        driver.find_element_by_xpath("//input[@value='3']").clear()
        driver.find_element_by_xpath("//input[@value='3']").send_keys("3")
        driver.find_element_by_xpath("//input[@value='5']").clear()
        driver.find_element_by_xpath("//input[@value='5']").send_keys("5")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[3]/input").clear()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[3]/input").send_keys("3")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[4]/input").clear()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[4]/input").send_keys("5")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div[2]/div/span").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div[2]/div/div/div/div/div/div[3]/div/div/div/span").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//input[@value='']").click()
        driver.find_element_by_xpath("//input[@value='3']").clear()
        driver.find_element_by_xpath("//input[@value='3']").send_keys("3")
        driver.find_element_by_xpath("//input[@value='5']").clear()
        driver.find_element_by_xpath("//input[@value='5']").send_keys("5")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[3]/input").clear()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[3]/input").send_keys("3")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[4]/input").clear()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div/div[4]/input").send_keys("5")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div/main/div[2]/div/div[2]/div/div/div/div[2]/div/span/div").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//button[@type='button']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_xpath("//div[@id='test-cards']/div/div/div/div[2]/span").click()
        driver.find_element_by_name("button").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath("//button[@type='button']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()