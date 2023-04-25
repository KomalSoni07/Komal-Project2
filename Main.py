#Komal_main

from selenium import webdriver
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
    
    def search_box(self):    
        self.driver.find_element_by_id('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
        assert search_box.is_displayed()

    def menu_options(self):
        menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "MyInfo", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]

for option in menu_options:
    # Type the menu option in the search box
    def search_box(self):
        search_box.clear()
        search_box.send_keys(option)
    
    # Wait for the search results to appear
    def search_result(self):
        self.driver.implicitly_wait(10)
        search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')))
    
    # Type a search term in lowercase
    def search_box(self):
        search_box.send_keys("example search term")
        search_box.send_keys(keys.RETURN)
 
    # Verify that the search results are displayed
    def search_results(self):
        self.driver.find_elements_by_class_name("search-result")
        assert len(search_results) > 0

# Clear the search box
search_box.clear()

# Type a search term in uppercase
def search_box(self):
    search_box.send_keys("EXAMPLE SEARCH TERM")
    search_box.send_keys(Keys.RETURN)

# Verify that the search results are displayed
def search_results(self):
    self.driver.find_elements_by_class_name("search-result")
    assert len(search_results) > 0

s = Komal(Komal_Data().url)


s.login()

