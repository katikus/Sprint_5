from time import sleep

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import urls, data
from helpers.locators import Locators


@pytest.mark.parametrize("from_url, to_url, locator, validator", [ #from_url начало теста, to_url - целевой url, locator - тригер перехода, validator ожидаемый на целевой странице элемент
    (urls.main_site_url, urls.profile_url_extended, Locators.MAIN_LK_BUTTON, Locators.LK_SAVE_BUTTON), # переход по клику на «Личный кабинет»
    (urls.profile_url, urls.main_site_url, Locators.CONSTRUCTOR, Locators.CREATE_ORDER_BUTTON), # переход по клику на «Конструктор»>
    (urls.profile_url, urls.main_site_url, Locators.LOGO, Locators.CREATE_ORDER_BUTTON), #переход по клику на логотип Stellar Burgers
    (urls.profile_url, urls.login_page_url, Locators.LK_LOGOUT, Locators.LOGIN_BUTTON) #выход по кнопке «Выйти» в личном кабинете.
])
def test_user_navigation(from_url, to_url, locator, validator, driver):
    #открываем окно логина
    driver.get(urls.login_page_url)

    # Ожидание появления кноки логина
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

    # Заполняем поля логин и пароль
    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_FIELD).send_keys(data.saved_email)
    driver.find_element(*Locators.LOGIN_PAGE_PASS_FIELD).send_keys(data.saved_pass)

    # Клик на кнопку логин
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Ожидание появления кнопки "Оформить заказ"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CREATE_ORDER_BUTTON))

    #Переход в проверяемый раздел
    driver.get(from_url)
    #sleep(5)
    driver.find_element(*locator).click()

    sleep(1)
    #Ожидание появления проверяемой сущности
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(validator))

    # Проверка что раздел соответсвует ожиданиям
    current_url = driver.current_url

    assert current_url == to_url