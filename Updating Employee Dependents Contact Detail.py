Komal_Main8

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
    
    def Dependents_contact_details(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewDependents/empNumber/10")
        self.driver.implicitly_wait(10)
        self.implicitly_wait.until(EC.presence_of_element_located((By.ID, "name")))
        
    def Dependents_contact_details(self):
        self.driver.find_element(By.ID, "name")
        self.name_field.send_keys("Mudasar Haq")
        self.driver.find_element(By.ID, "relationship")
        self.relationship_field.send_keys("Father")
        self.driver.find_element(By.ID, "dob")
        self.dob_field.send_keys("01/01/1980")
        self.driver.find_element(By.ID, "Action")
        self.action_field.send_keys("Yes")

    def save_button(self):
        self.driver.find_element(By.ID, "save-button")
        self.save_button.click()
        self.driver.implicitly_wait(10).until(EC.presence_of_element_located((By.ID, "assigned-dependent-details")))

# Verify the details are present
assert "Mudasar Haq" in assigned_dependent_details.text
assert "Father" in assigned_dependent_details.text
assert "01/01/1980" in assigned_dependent_details.text
assert "Yes" in assigned_dependent_details.text

s = Komal(Komal_Data().url)


s.login()
