Komal_Main9

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
    
    def Job_details(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewJobDetails/empNumber/10")
        self.driver.implicitly_wait(10)
        self.implicitly_wait.until(EC.presence_of_element_located((By.ID, "name")))
        
    def filled_Job_details(self):
        self.driver.find_element_by_name("Joined_Date")
        self.joined_date.send_keys("2021-02-23")
        self.driver.find_element_by_name("Job_Title")
        self.job_title.send_keys("QA Lead")
        self.driver.find_element_by_name("Job_Specification")
        self.job_specification.send_keys("Better Opportunity")
        self.driver.find_elements_by_name("Job_Category")
        self.job_category.send_keys("Professionals")
        self.driver.find_elements_by_name("Sub_Unit")
        self.sub_unit.send_keys("Quality_Assurance")
        self.driver.find_elements_by_name("Location")
        self.location.send_keys("New York Sales Office")
        self.driver.find_elements_by_name("Employment_Status")
        self.employment_status.send_keys("Full-Time Permanent")
        
    def toggle_button(self):
        self.driver.find_element_by_name("Include Employment Contract Details")
        self.include_employment_contract_details.click()

    def contract_details(self):
        self.driver.find_element_by_name("contract_start_date")
        self.contract_start_date.send_keys("2021-02-22")
        self.driver.find_element_by_name("contract_end_date")
        self.contract_end_date.send_keys("2021-02-28")

    def save_button(self):
        self.driver.find_element_by_id("save_button")
        self.save_button.click()
        self.driver.implicitly_wait(10)
        self.implicitly_wait.until(EC.presence_of_element_located((By.ID, "job_details")))

    def job_details_validation(self):
        self.driver.find_element_by_id("Joined_Date").text
        assert joined_date == "2021-02-23"
        self.driver.find_element_by_id("job_title").text
        assert job_title == "QA Lead."
        self.driver.find_element_by_id("job_specification").text
        assert Job_specification == "Better_Opportunity"
        self.driver.find_element_by_id("Job_Category").text
        assert salary_value == "Professionals"
        self.driver.find_element_by_id("Sub_Unit").text
        assert sub_unit == "Quality_Assurance"
        self.driver.find_element_by_id("Location").text
        assert location ==  "New York Sales Office"
        self.driver.find_element_by_id("Employment_status").text
        assert  employment_status == "Full-TimePermanent"
        

s = Komal(Komal_Data().url)


s.login()



