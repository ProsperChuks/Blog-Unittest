import unittest
from selenium import webdriver
import page

class blogsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://django-blog-app9.herokuapp.com/")

    def test_case1(self):
        hp = page.homePage(self.driver)
        assert hp.title_match()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
