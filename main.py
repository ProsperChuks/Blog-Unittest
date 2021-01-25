import unittest
from selenium import webdriver
import page

class blogsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://django-blog-app9.herokuapp.com/")

    def test_case1(self):
        homepage = page.homePage(self.driver)
        assert homepage.title_match()

    def test_case2(self):
        homepage = page.homePage(self.driver)
        homepage.click_1st_post()
        page_found = page.postResultPage(self.driver)
        assert page_found.isPageFound()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
