from selenium import selenium
import unittest
import re

class TestAdblock(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "http://addons.allizom.org")
        self.selenium.start()
        self.selenium.open("/")
        self.selenium.window_maximize()
        
    def tearDown(self):
        self.selenium.stop()
        
    def test_that_searching_for_adblocker_returns_the_result(self):
        self.selenium.type_keys("id=search-q", "adblock")
        self.selenium.click("search-button")
        self.selenium.wait_for_page_to_load("30000")
  
        result_in_page = self.selenium.is_text_present("Adblock Plus")
        self.assertTrue(result_in_page)
 
        self.assertEqual("Adblock Plus by Wladimir Palant", self.selenium.get_text("css=h3:first-child"))
    
        self.assertTrue(re.search(r"[0-9] weekly downloads", self.selenium.get_text("css=p.downloads")))
        pass
    
if __name__ == "__main__":
    unittest.main()
