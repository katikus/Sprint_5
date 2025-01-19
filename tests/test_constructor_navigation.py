from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import urls, data
from helpers.locators import Locators


def test_constructor_navigation(driver):
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

    # Переход в раздел Соусы
    driver.find_element(*Locators.MAIN_SAUCES_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        Locators.MAIN_SAUCE)), "не видно элемент MAIN_SAUCE"
    sleep(1)

    # Переход в раздел Булки
    driver.find_element(*Locators.MAIN_BUNS_BUTTON).click()
    #print((WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MAIN_KRATORS_BUNS))).text)
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        Locators.MAIN_KRATORS_BUNS)), "не видно элемент MAIN_KRATORS_BUNS"
    sleep(1)

    # Переход в раздел Начинки
    driver.find_element(*Locators.MAIN_TOPPING_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        Locators.MAIN_BIO_KOTLETA)), "не видно элемент MAIN_BIO_KOTLETA"
    sleep(1)