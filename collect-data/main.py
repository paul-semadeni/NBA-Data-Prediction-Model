"""
    Group Project
        Project Name: NBA Data Prediction Model
        Class: Intro to Data Analysis (CS6850)
        Instructor: Dr. Hamid Karimi
        Date: March 1, 2024
        Students: Paul Semadeni, Errick Aliifua
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

txt_box = driver.find_element(by=By.NAME, value="my-text")
submit_btn = driver.find_element(by=By.CSS_SELECTOR, value="button")

txt_box.send_keys("selenium")
submit_btn.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()