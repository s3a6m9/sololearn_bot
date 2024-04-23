"""
Author: s3a6m9
Last Edited: 22/04/2024
"""
from . import BasePage, sleep

PROFILE_URL = "https://www.sololearn.com/en/profile/"

COURSE_PROGRESS_MANAGE = """
//button[contains(@class, 'sl-p-courses__show-all') and text()='Manage']
"""
THREE_DOTS = """
//div[contains(@class, 'sl-p-all-progress-modal__body')]
//a[@href='/en/learn/courses/python-introduction?location=2']
//div[contains(@class, 'sl-opt-popover__dot')]
"""
RESTART_COURSE = """
//div[contains(@class, 'sl-p-all-progress-modal__body')]
//a[@href='/en/learn/courses/python-introduction?location=2']
//div[contains(@class, 'sl-opt-popover__menu-item') and contains(text(), 'Restart course')]
"""
RESTART_BUTTON = """
//button[contains(@class, 'sl-confirm-action__button') and contains(@class, 'sl-confirm-action__button--danger') and text()='Restart']
"""
COURSE_RESTARTED = """
//div[
    contains(@class, 'sl-shared-flash-message') and
    contains(@class, 'sl-shared-flash-message--success') and
    contains(@class, 'sl-shared-flash-message--shown') and
    text()='Course successfully restarted'
]
"""

class ProfilePage(BasePage):
    """A class representing the profile page of SoloLearn."""
    def __init__(self, browser):
        super().__init__(browser)
        self.page = PROFILE_URL

    def restart_python_course(self):
        """Restarts the intro to python course"""
        self.interact(COURSE_PROGRESS_MANAGE)
        self.interact(THREE_DOTS)
        self.interact(RESTART_COURSE)
        self.interact(RESTART_BUTTON)
        restarted = False
        while not restarted:
            if self.element_exists(COURSE_RESTARTED):
                break
            sleep(0.1)
