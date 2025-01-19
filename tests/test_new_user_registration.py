from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from generator import generate_email
from helpers import data

from helpers.locators import Locators

def test_new_user_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Генерирация email
    generated_email = generate_email()

    # Заполняем поля
    driver.find_element(*Locators.REG_NAME_FIELD).send_keys('Nikita')
    driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(generated_email)
    driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(data.saved_pass)

    # Нажимаем Зарегистрироваться
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()

    # Ждем обнаружения кнопки войти
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

    driver.find_element(*Locators.LOGIN_PAGE_EMAIL_FIELD).send_keys(generated_email)
    driver.find_element(*Locators.LOGIN_PAGE_PASS_FIELD).send_keys(data.saved_pass)

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CREATE_ORDER_BUTTON))

    assert 'Оформить заказ' in driver.find_element(*Locators.CREATE_ORDER_BUTTON).text

def test_new_user_registration_with_short_pass_(driver):
    wrong_pass = '12345'
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Генерирация email
    generated_email = generate_email()

    # Заполняем поля
    driver.find_element(*Locators.REG_NAME_FIELD).send_keys('Nikita')
    driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(generated_email)
    driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys(wrong_pass)

    driver.find_element(*Locators.REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_INCORRECT_PASSWORD_LABEL))
    assert  'Некорректный пароль' in  driver.find_element(*Locators.REGISTRATION_INCORRECT_PASSWORD_LABEL).text

