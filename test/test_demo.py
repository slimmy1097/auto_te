import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def before_test():
    print('before')
    yield
    print('\nafter test')


def test_demo1():
    assert 1 == 1


def test_demo2(before_test):
    assert 2 == 2
