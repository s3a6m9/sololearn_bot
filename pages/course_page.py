"""
Author: s3a6m9
Last Edited: 22/04/2024
"""
from . import sleep
from . import BasePage

COURSE_URL = "https://www.sololearn.com/en/learn/courses/python-introduction"

LEARN = "//button[text()='Learn']"
# Continue xpath is also the check button xpath, may be better to use an better selector
CONTINUE = "/html/body/div[1]/div/main/div[1]/div/div/footer/button"
FINISHED_LESSON_CONTINUE = "/html/body/div[1]/div/main/div[1]/div/div/div[2]/div/div/button"
DAILY_STREAK_CONTINUE = "/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div/div/button"
LEADERBOARD_CONTINUE = "/html/body/div[1]/div/main/div[1]/div/div/div/div[2]/div[2]/div/button"
AI_CHALLENGE_CONTINUE = "/html/body/div[1]/div/main/div[1]/div/div/div/div/div[2]/div[2]/div/button"

ANSWER_ONE = "/html/body/div[1]/div/main/div[1]/div/div/footer/div/div/div[1]"
ANSWER_TWO = "/html/body/div[1]/div/main/div[1]/div/div/footer/div/div/div[2]"
ANSWER_THREE = "/html/body/div[1]/div/main/div[1]/div/div/footer/div/div/div[3]"
ANSWER_FOUR = "/html/body/div[1]/div/main/div[1]/div/div/footer/div/div/div[4]"
ANSWER_FIVE = "/html/body/div[1]/div/main/div[1]/div/div/footer/div/div/div[5]"
ANSWER_SIX = "/html/body/div[1]/div/main/div[1]/div/div/footer/div/div/div[6]"

LADDER_ANSWER_ONE = "/html/body/div[1]/div/main/div[1]/div/div/div/div/div/div/div[3]/div[1]"
LADDER_ANSWER_TWO = "/html/body/div[1]/div/main/div[1]/div/div/div/div/div/div/div[3]/div[2]"
LADDER_ANSWER_THREE = "/html/body/div[1]/div/main/div[1]/div/div/div/div/div/div/div[3]/div[3]"
LADDER_ANSWER_FOUR = "/html/body/div[1]/div/main/div[1]/div/div/div/div/div/div/div[3]/div[4]"


class CoursePage(BasePage):
    """A class representing the introduction to python course page of SoloLearn."""
    def __init__(self, browser):
        super().__init__(browser)
        self.page = COURSE_URL

    def execute_steps(self, steps):
        """Executed steps in a list"""
        for step in steps:
            if step == "SLEEP":
                sleep(2)
                continue
            self.interact(step)
            print(step)
         #   input("Press enter for the next step")

    def do_writing_code_lesson(self):
        """Does the first "writing code" introduction to python lesson"""
        lesson_steps = [
            LEARN, # Click learn button
            "SLEEP",
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_TWO,  # (
            ANSWER_ONE,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # (
            ANSWER_THREE,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # "Order Shipped"
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # "
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # (
            ANSWER_TWO,  # "
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # "Wake up"
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # "Order ready"
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_TWO,  # (
            ANSWER_THREE,  #  360
            ANSWER_ONE,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            CONTINUE,  # Continue
            FINISHED_LESSON_CONTINUE  # Finish the lesson
        ]

        self.execute_steps(lesson_steps)

    def do_writing_code_lesson_ai(self):
        """Does writing code lesson ai challenge"""
        ai_challenge_steps = [
            AI_CHALLENGE_CONTINUE,  # Click AI challenge continue
            LADDER_ANSWER_ONE,  # Level Up
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # "New email"
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # (
            ANSWER_TWO,  # "
            ANSWER_THREE,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # "Turn right"
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # "
            ANSWER_THREE,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # (
            ANSWER_SIX,  #  7
            ANSWER_FIVE,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            ANSWER_ONE,  # print
            ANSWER_TWO,  # (
            ANSWER_THREE,  # "Great job!"
            ANSWER_FOUR,  # )
            CONTINUE,  # Check
            CONTINUE,  # Continue
            LADDER_ANSWER_TWO,  # to display the number  24 on the screen
            CONTINUE,  # Check
            CONTINUE,  # Continue
            FINISHED_LESSON_CONTINUE,  # Finish the lesson
            LEADERBOARD_CONTINUE  # Go to leaderboard  # sometimes isn't present
        ]

        self.execute_steps(ai_challenge_steps)
