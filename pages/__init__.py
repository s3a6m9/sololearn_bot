"""
Author: s3a6m9
Last Edited: 22/04/2024
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException,
                                        ElementNotInteractableException,
                                        NoSuchElementException,
                                        ElementClickInterceptedException)


class BasePage:
    """A base class for pages with common behavior."""
    def __init__(self, browser):
        self.driver = browser
        self.timeout = 10
        self.page = None  # Declared by child classes

    def open_page(self):
        """ Opens page """
        self.driver.get(self.page)

    def element_exists(self, xpath):
        """Returns True if element is found, otherwise False"""
        try:
            self.driver.find_element("xpath", xpath)
            return True
        except NoSuchElementException:
            return False

    def interact(self, xpath, action='click', text=None, retry=False):
        """Performs an interaction with an element located by xpath.

        Args:
            xpath (str):
                The XPath of the element to interact with.
            action (str, optional):
                The type of interaction ('click' or 'send_keys'). Defaults to 'click'.
            text (str, optional):
                The text to send to the element if action is 'send_keys'. Defaults to None.
            retry (bool, optional):
                Whether to retry the operation if it fails initially. Defaults to False.

        Raises:
            TimeoutException: If the element is not found within the timeout period.
            NoSuchElementException: If the element is not found.
            ElementNotInteractableException: If the element cannot be interacted with.
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            if action == 'click':
                element.click()

            elif action == 'send_keys':
                if text is not None:
                    element.send_keys(text)
                else:
                    raise ValueError("Text must be provided for 'send_keys' action.")
            else:
                raise ValueError(f"Invalid action '{action}'. Must be 'click' or 'send_keys'.")
        except (
            TimeoutException, NoSuchElementException,
            ElementNotInteractableException, ElementClickInterceptedException
            ) as e:
            if retry:
                print(f"Failed retrying element {xpath}: {str(e)}")
                raise e
            print(f"An error occurred while waiting for element {xpath}: {str(e)} \nRetrying Once")
            self.interact(xpath, action, text, retry=True)
