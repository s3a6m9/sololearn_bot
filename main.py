"""
Author: s3a6m9
Last Edited: 22/04/2024
"""
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.course_page import CoursePage
from pages.profile_page import ProfilePage
import config

EMAIL = config.EMAIL
PASSWORD = config.PASSWORD

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd("Network.setUserAgentOverride",
                      { "userAgent": driver.execute_script(
                          "return navigator.userAgent").replace("Headless", "")})


login_page = LoginPage(driver)
profile_page = ProfilePage(driver)
course_page = CoursePage(driver)

login_page.open_page()
input("Press enter once recaptcha is complete & the first lesson is introduction to python")
login_page.sign_in(EMAIL, PASSWORD)
time.sleep(2)
login_page.set_site_preferences()
time.sleep(2)

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
        driver.quit()
        break
    except Exception as e:
        print(e)
        time.sleep(10)
