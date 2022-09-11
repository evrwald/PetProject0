from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            'breadcrumb_header': '/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6',
            'profile_name': '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p',
            'profile_dropdown': '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i',
            'logout_btn': '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
        }

    def get_profile(self):
        return self.driver.find_element(By.XPATH, self.locators.get('profile_name')).text

    def get_breadcrumb_header(self):
        return self.driver.find_element(By.XPATH, self.locators.get('breadcrumb_header')).text

    def logout(self):
        profile_dropdown = self.driver.find_element(By.XPATH, self.locators.get('profile_dropdown'))
        profile_dropdown.click()
        try:
            logout_btn = WebDriverWait(self.driver,5).until(
                ec.presence_of_element_located((By.XPATH, self.locators.get('logout_btn')))
            )
            logout_btn.click()
        except Exception as e:
            print(str(e))
