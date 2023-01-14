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
        driver.get("https://admin.payfi.ng/")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("Olamide.john@payfi.ng")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Testqa1101$")
        driver.find_element_by_name("email").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/form/div/div[2]/div/button").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/button/span").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/span[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/button/span").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/li[2]/a/p").click()
        driver.find_element_by_name("search").click()
        driver.find_element_by_name("search").clear()
        driver.find_element_by_name("search").send_keys("olamide.john@payfi.ng")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr/td[3]/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[5]/div/div[4]/button").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[5]/div/div[4]/button[2]").click()
        driver.find_element_by_name("comment").click()
        driver.find_element_by_name("comment").clear()
        driver.find_element_by_name("comment").send_keys("tis is fine")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[5]/div/div[5]/div[2]/div/div[2]/div/div[5]/button").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[2]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[5]/div/div/div/div/div/p[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[3]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[4]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[6]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[5]/div/div/div[2]/div/div/div/div/table/tbody/tr/td[3]/p").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='olamide11 john11'])[1]/following::*[name()='svg'][2]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[7]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[5]/div/div/div[2]/div/div/div/div/table/tbody/tr/td[5]/p").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Loans'])[2]//*[name()='svg'][1]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[8]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[9]/a/p").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[3]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[3]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[4]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[5]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[6]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/p[2]").click()
        driver.find_element_by_name("search").click()
        driver.find_element_by_name("search").clear()
        driver.find_element_by_name("search").send_keys("PAYFI CREDIT CHECK")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr/td[2]/div/p[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[3]/div/div[2]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[3]/div/div[3]").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[3]/div/div[4]").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[4]/a/p").click()
        driver.find_element_by_name("search").click()
        driver.find_element_by_name("search").click()
        driver.find_element_by_name("search").clear()
        driver.find_element_by_name("search").send_keys("Olamide John")
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[2]/table/tbody[14]/tr/td[3]/p").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[5]/a/p").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[6]/a/p").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[7]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/ul/li[2]/a/p").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/ul/li/a/p").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("Olamide.john@payfi.ng")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Testqa1101$")

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