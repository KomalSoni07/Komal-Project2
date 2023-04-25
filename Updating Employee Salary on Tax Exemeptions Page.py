Komal Main13

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
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewUsTaxExemptions/empNumber/53")

    def add_button(self):
        self.driver.find_element_by_id("add_tax_exemptions_button")
        self.add_button.click()

    def federal_income_tax(self):
        self.driver.find_element_by_id("Status")
        self.status.send_keys("Not Applicable")
        self.driver.find_element_by_id("Exemption")
        self.exemption.send_keys("200")

    def state_income_tax(self):
        self.driver.find_element_by_id("State")
        self.state.send_keys("America")
        self.driver.find_elemnt_by_id("Status")
        self.status.send_keys("Not Applicable")
        self.driver.find_element_by_id("Exemptions")
        self.exemption.send_keys("200")
        self.driver.find_element_by_id("Unemployment State")
        self.unemployment_state.send_keys("Alaska")
        self.driver.find_element_by_id("Work State")
        self.work_state.send_keys("Arizona")
        
    def save_button(self):
        self.driver.find_element_by_id("save_button")
        self.save_button.click()

    def toggle_button(self):
        self.driver.find_element_by_id("direct_deposit_toggle_button")
        self.toggle_button.click()
        self.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "direct_deposit_fields")))

    def routing_number(self):
        self.driver.find_element_by_id("routing_number")
        self.routing_number.send_keys("123456789")
        
    def account_number(self):
        self.driver.find_element_by_id("account_number")
        self.account_number.send_keys("987654321")
    
    def account_type(self):
        self.driver.find_element_by_id("account_type")
        self.acount_type.send_keys("savings")
    
    def amount(self):
        self.driver.find_element_by_id("Amount")
        self.amount.send_keys("20000")

    def save_button(self):
        self.driver.find_element_by_id("save_button")
        self.save_button.click()
        self.WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "saved_values")))
        assert saved_values.text == "Component1: $1000\nComponent2: $2000\nRouting Number: 123456789\nAccount Number: 987654321"

s = Komal(Komal_Data().url)


s.login()