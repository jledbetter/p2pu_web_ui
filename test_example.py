from selenium import selenium
import unittest
import re

class TestGoogle(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "http://google.com")
        self.selenium.start()
        self.selenium.open("/")
        self.selenium.window_maximize()
        
    def tearDown(self):
        self.selenium.stop()
        
    def test_that_searching_for_selenium_returns_the_result(self):
        self.selenium.type("q", "selenium")
        self.selenium.click("btnG")
  
        result_in_page = self.selenium.is_text_present("Selenium web application testing system")
        self.assertTrue(result_in_page)
        
        pass
    
if __name__ == "__main__":
    unittest.main()
