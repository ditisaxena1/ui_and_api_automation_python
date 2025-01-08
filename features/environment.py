import logging
import os
from datetime import datetime

from selenium import webdriver


def before_all(context):
    context.config.setup_logging()

    screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    context.screenshot_dir = screenshot_dir

    context.base_url = "https://ebay.com"
    context.api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"


def before_scenario(context, scenario):
    if "web" in scenario.tags:
        logging.info(f"Running Scenario -- {scenario.name}")
        print(f"Running Scenario -- {scenario.name}")

        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(2)
        context.driver.get(context.base_url)


def after_step(context, step):

    if step.status == "failed":
        time_stamp = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        screenshot_path = os.path.join(context.screenshot_dir, f"Failed: {step.name}_{time_stamp}.png")
        logging.info("taking screenshot")
        context.driver.save_screenshot(screenshot_path)


def after_scenario(context, scenario):
    if "web" in scenario.tags:
        logging.info(f"Ending Scenario -- {scenario.name}")

        if context.driver:
            context.driver.close()
            context.driver.quit()