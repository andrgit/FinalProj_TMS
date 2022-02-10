import psycopg2

import pytest
from selenium import webdriver


# @pytest.fixture(scope='session')
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--remote-debugin-port=9222")
    options.add_argument("--screen-size=1200x800")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield


@pytest.fixture(scope='session')
def connect_to_db():
    connection = psycopg2.connect(dbname='postgres', user='postgres',
                                  password='postgres', host='localhost')
    db_session = connection.cursor()
    yield db_session
    connection.close()
