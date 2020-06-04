import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Start")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://helion.pl/users/rejestracja.cgi")
        self.driver.maximize_window()

    def testSelenium(self):
        driver = self.driver

        print("Poszukiwania")
        email = driver.find_element_by_id("email")
        email.click()
        email.send_keys("kasia.zawialo@yopmail.com")
        passone = driver.find_element_by_id("haslo1")
        passone.click()
        passone.send_keys("kasia.zawialo")
        passtwo = driver.find_element_by_id("haslo2")
        passtwo.click()
        passtwo.send_keys("kasia.zawialoo")
        select = driver.find_element_by_id("checkall")
        select.click()
        zaloguj=driver.find_element_by_xpath('//p[text()="Zakładam konto"]')
        sleep(10)
        zaloguj.click()



    def tearDown(self):
        print("the_end")
        self.driver.quit()




if __name__=='__main__':
    unittest.main()
