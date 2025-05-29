from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators."""
    ID_TXT = (By.ID, "txtDashId")
    USER_TXT = (By.ID, "txtUserName")
    PW_TXT = (By.ID, "txtPassword")
    LOGIN_BTN = (By. ID, "btnLogIn")

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
