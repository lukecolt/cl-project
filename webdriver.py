from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://www.google.com")
        time.sleep(5)

    def test_findlogobyxpath(self):
        logo = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/img")
        self.assertEqual(True, logo.is_displayed(),"Google logo wasn't displayed")

    def tearDown(self):
        self.driver.close()

class CodelabSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://www.google.com")
        time.sleep(5)

    def test_searchcodelab(self):
        elem = self.driver.find_element(By.NAME, "q")
        elem.send_keys("codelab.eu")
        elem.submit() 
        logo_cl = self.driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/div/span/div/img")
        self.assertEqual(True, logo_cl.is_displayed(),"Codelab logo wasn't displayed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()




