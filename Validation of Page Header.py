Komal_main2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Komal_Data
from Test_Locators.locators import Komal_Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    

    def users_link(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a')
        users_link.click()

    def user_role(self):
        self.driver.find_element_by_xpath("//label[text()='User Role']/following-sibling::div/select")
        user_role_options = [option.text for option in user_role_field.find_elements_by_tag_name("option")]
        assert "Admin" in user_role_options
        assert "ESS" in user_role_options

    def status_field(self):
        self.driver.find_element_by_xpath("//label[text()='Status']/following-sibling::div/select")
        status_options = [option.text for option in status_field.find_elements_by_tag_name("option")]
        assert "Enabled" in status_options
        assert "Disabled" in status_options

s = Komal(Komal_Data().url)


s.login()