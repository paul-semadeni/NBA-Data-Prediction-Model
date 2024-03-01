"""
    Scrape data from NBA.com
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import subprocess
from config.nba_dot_com_config import NBA_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"

service = webdriver.ChromeService(log_output=subprocess.STDOUT)
driver = webdriver.Chrome(service=service, options=options)

driver.get(NBA_URL)

title = driver.title

driver.implicitly_wait(0.5)

# txt_box = driver.find_element(by=By.NAME, value="my-text")
# submit_btn = driver.find_element(by=By.CSS_SELECTOR, value="button")

# txt_box.send_keys("selenium")
# submit_btn.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

driver.quit()