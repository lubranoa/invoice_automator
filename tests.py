import os
from dotenv import load_dotenv
import unittest
from selenium import webdriver
import page

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
COMPANY_ID = os.getenv("COMPANY_ID")
USER = os.getenv("USER")
KEY = os.getenv("KEY")

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BASE_URL)

    def test_load_login(self):
        """Tests loading login page for FRSTAid. Verifies the title of the
        page equals	'Powered by Next Gear Solutions'"""
        
        # Load the main page. In this case the home page of frstaid-ngs.net
        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "website title doesn't match.")
    
    def test_find_company_id_input(self):
        """Tests finding the Company ID input box and entering a value.
        Verifies the company ID equals the one in .env"""

        login_page = page.MainPage(self.driver)
    
    def test_search_for_job(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        # Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "website title doesn't match.")
        # Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
