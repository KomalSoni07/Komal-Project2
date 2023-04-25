Komal_Main5

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
    
    def personal_details(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/10")
        self.driver.implicitly_wait(10)
        self.implicitly_wait.until(EC.presence_of_element_located((By.ID, "first_name")))

    def fillout_fields(self):
        self.driver.find_element_by_id("first_name")
        self.first_name.send_keys("Aaliyah")
        self.driver.find_element_by_id("last_name")
        self.last_name.send_keys("Haq")
        self.driver.find_element_by_id("employee_id")
        self.employee_id.send_keys("0038")
        self.driver.find_element_by_id("phone")
        self.phone.send_keys("123-456-7890")
        self.driver.find_element_by_id("Nationality")
        self.nationality.send_keys("Australian")
        self.driver.find_element_by_id("Marital_status")
        self.marital_status.send_keys("Single")
        self.driver.find_element_by_id("Gender")
        self.gender.send_keys("Female")
    
    def save_button(self):
        self.driver.find_element_by_id("save_button")
        self.save_button.click()
        self.driver.implicitly_wait(10)

    assert first_name.get_attribute("value") == "Aaliyah"
    assert last_name.get_attribute("value") == "Haq"
    assert employee_id.get_attribute("value") == "0038"
    assert phone.get_attribute("value") == "123-456-7890"
    assert nationality.get_attribute("value") == "Australian"
    assert marital_status.get_attribute("value") == "Single"
    assert gender.get_attribute("value") == "Female"
    

s = Komal(Komal_Data().url)


s.login()

