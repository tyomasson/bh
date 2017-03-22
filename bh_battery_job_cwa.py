# -*- coding: utf-8 -*-
# Create Battery job for Flow A
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


class Bh1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://staging-app.breakdownhero.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_bh_py(self):
        driver = self.driver
        driver.get(self.base_url + "/#/newJob/")
        wait = WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.safety-title.hide-show-animate.col-xs-12.ng-hide')))
        driver.find_element_by_class_name("manual-location-link").click()
        #Delete click block
        js = "var aa=document.getElementsByClassName('click-block')[0];aa.parentNode.removeChild(aa)"
        driver.execute_script(js)
        #--------------
        driver.find_element_by_class_name("location-field").click()
        driver.find_element_by_id("location").click()
        driver.find_element_by_id("location").clear()
        driver.find_element_by_id("location").send_keys("London")
        driver.find_element_by_id("b1a8b96daab5065cf4a08f953e577c34cdf769c0").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.problem-image.battery").click()
        driver.find_element_by_xpath("//div[3]/button").click()
        time.sleep(1)
        driver.find_element_by_id("vehicle_registration").click()
        driver.find_element_by_id("vehicle_registration").clear()
        driver.find_element_by_id("vehicle_registration").send_keys("234dle")
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys("2222222")
        driver.find_element_by_xpath("//div[3]/div/button").click()
        time.sleep(1)
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys("Auto")
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys("Test")
        driver.find_element_by_id("card_number").clear()
        driver.find_element_by_id("card_number").send_keys("4242 4242 4242 4242")
        driver.find_element_by_id("date").clear()
        driver.find_element_by_id("date").send_keys("12 / 21")
        driver.find_element_by_id("cvv").clear()
        driver.find_element_by_id("cvv").send_keys("121")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//ion-nav-view/ion-view/ion-footer-bar/button").click()
        driver.find_element_by_xpath(".//div[@class='layout-wrapper']//div[2]").click()
        driver.find_element_by_id("anything").clear()
        driver.find_element_by_id("anything").send_keys("test")
        driver.find_element_by_xpath("//ion-view[3]/ion-footer-bar/button").click()
        driver.find_element_by_xpath("(//div/label[@class='ng-binding'])[1]").click()
        driver.find_element_by_xpath("//ion-view[4]/ion-footer-bar/button").click()
        time.sleep(5)

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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
