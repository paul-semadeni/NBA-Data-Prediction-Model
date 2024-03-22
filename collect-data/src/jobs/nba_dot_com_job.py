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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# options = webdriver.ChromeOptions()
# options.page_load_strategy = "eager"

# service = webdriver.ChromeService(log_output=subprocess.STDOUT)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome()

driver.get(NBA_URL)

try:
    # Change pagination to all items
    driver.implicitly_wait(10)
    pagination_div = driver.find_element(By.XPATH, "//section[contains(@class, 'nba-stats-content-block')]")
    select_element = pagination_div.find_element(By.CLASS_NAME, "DropDown_select__4pIg9")
    select = Select(select_element)
    driver.implicitly_wait(0.5)
    select.select_by_value("-1")

    # Scrape all table rows
    driver.implicitly_wait(0.5)
    table_id = driver.find_element(By.XPATH, "//table[contains(@class,'Crom_table')]")
    rows = table_id.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        print(row.text)
except Exception as e:
    print(str(e))
    driver.quit()
else:
    print("Finished job")
    driver.quit()
