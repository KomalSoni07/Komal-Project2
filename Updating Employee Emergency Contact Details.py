Komal_Main7

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
    
    def Emergency_contact_details(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmergencyContacts/empNumber/10")
        self.driver.implicitly_wait(10)
        self.implicitly_wait.until(EC.presence_of_element_located((By.ID, "first_name")))


    def filled_fields(self):
        self.driver.find_element_by_id("Name")
        self.name.send_keys("Mushdiq Haq")
        self.driver.find_element_by_id("Relationship")
        self.relationship.send_keys("Brother")
        self.driver.find_element_by_id("Home Telephone")
        self.home_telephone.send_keys("134568")
        self.driver.find_element_by_id("Actions")
        self.actions.send_keys("No")

    def save_button(self):
        self.driver.find_element_by_id("save_button")
        self.save_button.click()
        self.driver.implicitly_wait(10)

        assert name.get_attribute("value") == "Mushdiq Haq"
        assert relationship.get_attribute("value") == "Brother"
        assert home_telephone.get_attribute("value") == "134568"
        assert actions.get_attribute("value") == "No"

s = Komal(Komal_Data().url)


s.login()