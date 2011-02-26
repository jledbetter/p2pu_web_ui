from selenium import selenium
import unittest

class TestInputStageSite(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium("localhost", 4444, 
                        "*firefox", "http://input.stage.mozilla.com")
        self.selenium.start()
        self.selenium.open("/")
        self.selenium.window_maximize()
        
    def tearDown(self):
        self.selenium.stop()
        
    def test_that_clicking_on_a_language_checkbox_makes_other_language_choices_disappear(self):
        self.selenium.click("loc_ru")
        self.selenium.wait_for_page_to_load("30000")
        """
         wanted to assertFalse(self.selenium.click("loc_en-US")) to make sure can't
         but get not found for element which is right
        """
        self.assertFalse(self.selenium.is_element_present("loc_en-US"))
        self.selenium.click("loc_ru")
        self.selenium.wait_for_page_to_load("30000")
        self.assertTrue(self.selenium.is_element_present("loc_en-US"))
    pass
        
if __name__ == "__main__":
    unittest.main()
