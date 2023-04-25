Komal_Main10

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
    
    def terminate_button(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button')
        self.terminate_button.click()

    def termination_date(self):
        self.driver.find_element_by_name('termination_date')
        self.termination_date.send_keys('2023-03-21')
        self.driver.find_element_by_name('termination_reason')
        self.termination_reason.send_keys('Employee requested termination')
        
    def save_button(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]')
        self.save_button.click()

    def terminated_on(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p')
        assert terminated_on.text == 'Terminated on 2023-03-21'
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button')
        assert activate_employment.is_displayed()


s = Komal(Komal_Data().url)


s.login()

