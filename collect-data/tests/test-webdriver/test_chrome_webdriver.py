"""
    Test Chrome Webdriver
    Source: https://testdriven.io/blog/modern-tdd/
"""
import pytest
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_log_to_stdout(capfd):
    service = webdriver.ChromeService(log_output=subprocess.STDOUT)

    driver = webdriver.Chrome(service=service)

    out, error = capfd.readouterr()
    assert "Starting ChromeDriver" in out

    driver.quit()
