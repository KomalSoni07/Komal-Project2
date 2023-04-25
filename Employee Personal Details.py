Komal_Main4

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

    def employee_list_menu(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')
        employee_list_menu.click()

tabs = ["Personal Details", "Contact Details", "Emergency Contacts", "Dependents", "Immigration",
        "Job", "Salary", "Tax Exemptions", "Report-to", "Qualifications", "Memberships"]

for tab in tabs:
    def tab_link(self):
        self.driver.find_element_by_xpath(f'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
        tab_link.click()
    
    def tab_content(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]')
        assert tab_content.is_displayed(), f"{tab} tab content is not displayed"


s = Komal(Komal_Data().url)


s.login()


