import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# sleep(2)
# import time ->  time.sleep(2)

class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Start")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://helion.pl/")
        self.driver.maximize_window()

    def testSelenium(self):
        driver = self.driver

        print("Poszukiwania")
        search = driver.find_element_by_id("inputSearch")
        search.click()
        search.send_keys("Selenium. Automatyczne testowanie aplikacji")
        sleep(5)
        search_btn = driver.find_element_by_class_name('button')
        sleep(3)
        search_btn.click()
        search.submit()
        sleep(3)

        print("Wybor_produktu")
        wybierz_produkt=driver.find_element_by_link_text('Selenium. Automatyczne testowanie aplikacji')
        wybierz_produkt.click()


        print("rodo")
        rodo = driver.find_element_by_id("rodo-ok")

        rodo.click()

        kup = driver.find_element_by_id("addToBasket_selata_ebook")
        sleep(3)
        kup.click()

        zamow = driver.find_element_by_xpath("//div/p/button[@type='submit']")
        sleep(5)
        zamow.click()
        sleep(5)
        zarejestruj = driver.find_element_by_link_text('Zarejestruj się')

        zarejestruj.click()
        #sleep(3)
        email = driver.find_element_by_id("email")
        email.click()
        email.send_keys("kasia.zawialo@yopmail.com")
        passone = driver.find_element_by_id("haslo1")
        passone.click()
        passone.send_keys("kasia.zawialo")
        passtwo = driver.find_element_by_id("haslo2")
        passtwo.click()
        passtwo.send_keys("kasia.zawialo")


        select = driver.find_element_by_id("checkall")
        select.click()

        zaloguj=driver.find_element_by_xpath("//div/p/button[@type='submit']")
        zaloguj.click()

    def tearDown(self):
        print("the_end")
        self.driver.quit()



if __name__=='__main__':
    unittest.main()
