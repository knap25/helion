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
        sleep(2)
        search_btn.click()
        search.submit()
        sleep(3)

        print("Wybor_produktu")
        wybierz_produkt=driver.find_element_by_link_text('Selenium. Automatyczne testowanie aplikacji')
        wybierz_produkt.click()


        print("zaakceptuj_rodo")
        rodo = driver.find_element_by_id("rodo-ok")
        rodo.click()

        print("dodaj_do_koszyka")
        kup = driver.find_element_by_id("addToBasket_selata_ebook")
        sleep(3)
        kup.click()

        print("Zamawiam")
        zamow = driver.find_element_by_xpath("//div/p/button[@type='submit']")
        sleep(5)
        zamow.click()


        print("Zarejestruj_się")
        zarejestruj = driver.find_element_by_link_text('Zarejestruj się')
        zarejestruj.click()

        print("zaloz_konto")
        email = driver.find_element_by_id("email")
        email.click()
        email.send_keys("kasia.zawialo@yopmail.com")
        passone = driver.find_element_by_id("haslo1")
        passone.click()
        passone.send_keys("kasia.zawialo")
        passtwo = driver.find_element_by_id("haslo2")
        passtwo.click()
        passtwo.send_keys("kasia.zawialo")

        print("akceptuj_oswiadczenia")
        select = driver.find_element_by_id("checkall")
        select.click()

        print("zakoncz_rejestracje")
        rejestracja=driver.find_element_by_xpath("//div/p/button[@type='submit']")
        rejestracja.click()
        
    def tearDown(self):
        print("the_end")
        self.driver.quit()



if __name__=='__main__':
    unittest.main()
