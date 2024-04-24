"""
Author: s3a6m9
Last Edited: 24/04/2024
"""
from . import BasePage

LOGIN_URL = "https://www.sololearn.com/en/users/login"

EMAIL_INPUT = "//*[@id='email']"
PASSWORD_INPUT = "//*[@id='password']"
LOG_IN_BUTTON = "//button[text()='Log in']"
STATISTICS_BOX = "//input[@id='CybotCookiebotDialogBodyLevelButtonStatistics']"
MARKETING_BOX = "//input[@id='CybotCookiebotDialogBodyLevelButtonMarketing']"
OK_BUTTON = "//a[@id='CybotCookiebotDialogBodyLevelButtonAccept']"


class LoginPage(BasePage):
    """A class representing the login page of SoloLearn."""
    def __init__(self, browser):
        super().__init__(browser)
        self.page = LOGIN_URL

    def set_site_preferences(self):
        """ Sets site preferences """
        self.interact(MARKETING_BOX)
        self.interact(STATISTICS_BOX)
        self.interact(OK_BUTTON)

    def sign_in(self, email, password):
        """ Signs into Sololearn """
        self.interact(xpath=EMAIL_INPUT, action="send_keys", text=email)
        self.interact(xpath=PASSWORD_INPUT, action="send_keys", text=password)
        print("\nPressing 'Log in'.")
        self.interact(LOG_IN_BUTTON)
