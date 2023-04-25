Komal_Main6

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Komal_Data
from Test_Locators.locators import Komal_Locators
from selenium.webdriver.support import expected_conditions as EC

class Komal:
       
    def __init__(self, url):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)
   
    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Komal_Locators().username_input_box).send_keys(Komal_Data().username)
        self.driver.find_element(by=By.NAME, value=Komal_Locators().password_input_box).send_keys(Komal_Data().password)
        self.driver.find_element(by=By.XPATH, value=Komal_Locators().submit_button).click()
        
    def contact_details(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/contactDetails/empNumber/10")
        self.driver.implicitly_wait(10)
        self.implicitly_wait.until(EC.presence_of_element_located((By.ID, "first_name")))


    def filled_fields(self):
        self.driver.find_element_by_id("address")
        self.address.send_keys("123 Main St")
        self.driver.find_element_by_id("telephone")
        self.telephone.send_keys("7845263")
        self.driver.find_element_by_id("email")
        self.email.send_keys("aaliyah1@osohrm.com")
        self.driver.find_element_by_id("zip_code")
        self.zip_code.send_keys("12345")

    def save_button(self):
        self.driver.find_element_by_id("save_button")
        self.save_button.click()
        self.driver.implicitly_wait(10)

        assert address.get_attribute("value") == "123 Main St"
        assert telephone.get_attribute("value") == "7845263"
        assert email.get_attribute("value") == "aaliyah1@osohrm.com"
        assert zip_code.get_attribute("value") == "12345"

s = Komal(Komal_Data().url)


s.login()
