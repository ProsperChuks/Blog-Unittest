from locator import *

class basePage(object):

    def __init__(self, driver):
        self.driver = driver
    

class homePage(basePage):

    def title_match(self):
        return "Application" in self.driver.title

    def click_1st_post(self):
        element = self.driver.find_element(*homePageLocators.FIRST_POST)
        element.click()

class postResultPage(basePage):

    def isPageFound(self):
        return "No result found" not in self.driver.page_source

