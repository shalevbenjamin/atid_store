import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from my_driver import driver_setup

link = 'https://atid.store/'

class End_to_end(unittest.TestCase):

    def setUp(self) -> None:
        self.my_driver = driver_setup()
        self.my_driver.get(link)

    def test_add_product(self):
        shop_now = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="post-2888"]/div/div/section[1]/div[2]/div/div/div[4]/div/div/a')))
        shop_now.click()

        atid_black_shoes = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/ul/li[2]/div[2]/a/h2')))
        atid_black_shoes.click()

        add_to_cart = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="product-375"]/div[2]/form/button')))
        add_to_cart.click()

        view_cart = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[1]/div/a')))
        view_cart.click()


    def test_check_out(self):
        self.test_add_product()

        proceed_to_checkout = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="post-39"]/div/div/section[2]/div/div/div/div/div/div/div/div[2]/div/div/a')))
        proceed_to_checkout.click()

        first_name = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'billing_first_name')))
        first_name.send_keys('harel')

        last_name = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'billing_last_name')))
        last_name.send_keys('koki')

        country = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="billing_country_field"]/span/span/span[1]/span')))
        country.click()

        country_choice = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/span[2]/span/span[1]/input')))
        country_choice.send_keys('israel')
        country_choice.send_keys(Keys.RETURN)

        street_address = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'billing_address_1')))
        street_address.send_keys('lolo')

        street_address_2 = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'billing_address_2')))
        street_address_2.send_keys('zing 2')

        postcode = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'billing_postcode')))
        postcode.send_keys('1231')

        city = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'billing_city')))
        city.send_keys('tel aviv')

        city = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'billing_phone')))
        city.send_keys('054-7878755')

        email = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'billing_email')))
        email.send_keys('ssdd@gmail.co.il')

        place_order = WebDriverWait(self.my_driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'place_order')))
        place_order.click()









    def tearDown(self) -> None:
        time.sleep(5)
        self.my_driver.quit()


        #hello worl


        #2