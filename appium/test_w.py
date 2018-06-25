
from appium import webdriver
import test_a

driver = test_a.a_url()


def click_id(key):
    driver.find_element_by_id(key).click()
    # return value


def click_class(key):
    value = driver.find_element_by_class_name(key).click()
    return value


def click_xpath(key):
    value = driver.find_element_by_xpath(key).click()
    return value


def click_text(key):
    value = driver.find_elements_by_android_uiautomator(
        "new UiSelector().text(\'"+key+"\')")[0].click()
    return value
# def click_id ():
