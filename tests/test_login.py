from utilities.driver_manager import DriverManager as dm
from utilities.data_provider import DataProvider as dp
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
import allure


class TestLogin:
    @allure.title("""Login as Admin""")
    def test_login_as_admin(self):
        admin_profile = dp.get_credentials('Admin').get('profile')
        driver = dm.get_driver()
        login_page = LoginPage(driver)
        login_page.login('Admin')
        pim_page = PIMPage(login_page.driver)
        try:
            assert pim_page.get_profile() == admin_profile
        finally:
            driver.quit()

    @allure.title("""Attempt login with incorrect Username""")
    def test_wrong_username_login(self):
        driver = dm.get_driver()
        login_page = LoginPage(driver)
        login_page.login('Wrong_User')
        try:
            assert login_page.get_error() == 'Invalid credentials'
        finally:
            driver.quit()

    @allure.title("""Attempt login with incorrect password""")
    def test_wrong_password_login(self):
        driver = dm.get_driver()
        login_page = LoginPage(driver)
        login_page.login('Wrong_Password')
        try:
            assert login_page.get_error() == 'Invalid credentials'
        finally:
            driver.quit()

    @allure.title("""Login as Admin and logout""")
    def test_logout(self):
        driver = dm.get_driver()
        login_page = LoginPage(driver)
        login_page.login('Admin')
        pim_page = PIMPage(login_page.driver)
        pim_page.logout()
        try:
            assert login_page.get_header() == 'Login'
        finally:
            driver.quit()
