from selenium.webdriver.common.by import By
from utilities.data_provider import DataProvider as dm
from utilities.property_reader import PropertyReader as pr
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            'username_input': 'username',
            'password_input': 'password',
            'login_btn': '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button',
            'error_message': '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p',
            'header': '/html/body/div/div[1]/div/div[1]/div/div[2]/h5'
        }

    def login(self, user):
        self.load(pr.read_property('config.properties', 'base_url'))
        credentials = dm.get_credentials(user)
        try:
            username_input = WebDriverWait(self.driver, 5).until(
                ec.presence_of_element_located((By.NAME, self.locators.get('username_input')))
            )
            username_input.send_keys(credentials.get('username'))
            password_input = self.driver.find_element(By.NAME, self.locators.get('password_input'))
            password_input.send_keys(credentials.get('password'))
            login_btn = self.driver.find_element(By.XPATH, self.locators.get('login_btn'))
            login_btn.click()
        except Exception as e:
            print(str(e))

    def get_error(self):
        try:
            error_message = WebDriverWait(self.driver, 5).until(
                ec.presence_of_element_located((By.XPATH, self.locators.get('error_message')))
            )
            return error_message.text
        except Exception as e:
            print(str(e))

    def get_header(self):
        return self.driver.find_element(By.XPATH, self.locators.get('header')).text
