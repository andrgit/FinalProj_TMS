import psycopg2

import pytest
from selenium import webdriver


# @pytest.fixture(scope='session')
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

#Start on Mac (jenkins)
@pytest.fixture(scope='session')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def connect_to_db():
    connection = psycopg2.connect(dbname='postgres', user='postgres',
                                  password='postgres', host='localhost')
    db_session = connection.cursor()
    yield db_session
    connection.close()
