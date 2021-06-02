import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="session") #декоратор на 1 использование за запуск
def browser():
    exec_path = os.getcwd()
    driver = webdriver.Chrome(executable_path=exec_path + "\\chromedriver.exe")
    yield driver
    driver.quit()
