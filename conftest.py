import psycopg2

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def connect_to_db():
    connection = psycopg2.connect(dbname='postgres', user='postgres',
                                  password='postgres', host='localhost')
    db_session = connection.cursor()
    yield db_session
    connection.close()
