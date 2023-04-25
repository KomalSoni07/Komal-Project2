Komal_Main3

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

    def pim_menu(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        pim_menu.click()

    def add_button(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        add_button.click()

    def create_login_checkbox(self):
        self.driver.find_element_by_xpath("//input[@id='chkLogin']")
        create_login_checkbox.click()

    def details(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        first_name_field.send_keys("John")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
        last_name_field.send_keys("Doe")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
        employee_id_field.send_keys("1234")

    def status_radio_button(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
        status_radio_button.click()

    def login_details(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
        username_field.send_keys("johndoe")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
        password_field.send_keys("password123")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
        confirm_password_field.send_keys("password123")

    def save_button(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
        save_button.click()

s = Komal(Komal_Data().url)


s.login()