from selenium import webdriver


class DriverManager:
    @staticmethod
    def get_driver(browser='Chrome'):
        if browser == 'Firefox':
            return webdriver.Firefox()
        else:
            return webdriver.Chrome()
