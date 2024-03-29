"""
    Scrape data from NBA.com
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pandas as pd
import subprocess
import time
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
nba_stats = pd.DataFrame()

try:
    # Change season years
    driver.implicitly_wait(0.5)
    season_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'Block_block__62M07')]"))
    )
    select_year = season_div.find_element(By.CLASS_NAME, "DropDown_select__4pIg9")
    select = Select(select_year)
    option_list = select.options
    for n in range(len(option_list)):
        season_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'Block_block__62M07')]"))
        )
        select_year = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "DropDown_select__4pIg9"))
        )
        time.sleep(8)
        select = Select(select_year)
        opt = select.options[n]
        season = opt.text
        select.select_by_value(season)
        # Change pagination to all items
        pagination_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'nba-stats-content-block')]"))
        )
        time.sleep(8)
        select_all = pagination_div.find_element(By.CLASS_NAME, "DropDown_select__4pIg9")
        select = Select(select_all)
        select.select_by_value("-1")

        # Scrape all table rows
        table_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@class,'Crom_table')]"))
        )
        rows = table_id.find_elements(By.TAG_NAME, "tr")
        # Store season stats
        temp_dict = {"columns": [], "data": []}
        # Use to assign first list as column names in dataframe
        i = 0
        for row in rows:
            temp_list = row.text.split(" ")
            temp_list.append(season)
            if len(temp_list) > 33:
                temp_list.pop(2)
                temp_list.pop(3)

            if len(temp_list) < 33:
                temp_list.insert(3, "")

            if i <= 0:
                temp_list[0] = "RANK"
                temp_list[1] = "FIRST NAME"
                temp_list[2] = "LAST NAME"
                temp_list[3] = "SUFFIX"
                temp_list[32] = "SEASON"
                temp_dict["columns"] = temp_list
            else:
                temp_dict["data"].append(temp_list)
            i += 1
        temp_df = pd.DataFrame(temp_dict["data"], columns=temp_dict["columns"])
        print(season)
        nba_stats = pd.concat([nba_stats, temp_df], ignore_index=True, sort=False)
except Exception as e:
    print(str(e))
    print(nba_stats)
    driver.quit()
else:
    print("Finished job")
    driver.quit()

cwd = os.getcwd()
nba_stats.to_excel(cwd + "/collect-data/src/files/nba_data.xlsx", sheet_name="NBA Stats")
