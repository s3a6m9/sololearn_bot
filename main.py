"""
Author: s3a6m9
Last Edited: 24/04/2024
"""
import time
import sys
import os
from selenium import webdriver
from pages.login_page import LoginPage
from pages.course_page import CoursePage
from pages.profile_page import ProfilePage
try:
    import config
except ImportError:
    print("Config file does not exist, creating it now.")
    with open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "config.py"),
        "w", encoding="utf8"
    ) as config:
        config.write("\"\"\" Sololearn account credentials & Other configurations \"\"\"\nEMAIL = ''\nPASSWORD = ''\n")
    sys.exit(1)

EMAIL = config.EMAIL
PASSWORD = config.PASSWORD

if EMAIL == "" or PASSWORD == "":
    print("Please add an email/password to config.py")
    sys.exit(1)

options = webdriver.ChromeOptions()
chrome_args = [
"--window-size=1000,1050",
"--window-position=0,0",
# "--headless=new",  # not tested
]
for arg in chrome_args:
    options.add_argument(arg)

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Network.setUserAgentOverride",
                      { "userAgent": driver.execute_script(
                          "return navigator.userAgent").replace("Headless", "")})

login_page = LoginPage(driver)
profile_page = ProfilePage(driver)
course_page = CoursePage(driver)

login_page.open_page()
time.sleep(2)
login_page.set_site_preferences()
input("Press enter once recaptcha is complete & introduction to python is in managed courses")
login_page.sign_in(EMAIL, PASSWORD)
time.sleep(2)
print("Should be logged in.")

while True:
    try:
        profile_page.open_page()
        profile_page.restart_python_course()
        course_page.open_page()
        time.sleep(1)
        course_page.do_writing_code_lesson()
        time.sleep(1)
        course_page.do_writing_code_lesson_ai()
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected, quitting.")
        driver.quit()
        break
    except Exception as e:
        print(e)
        time.sleep(10)
