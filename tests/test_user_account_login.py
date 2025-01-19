import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import urls
from helpers.locators import Locators


@pytest.mark.parametrize("url, locator", [
    (urls.main_site_url, Locators.MAIN_LOGIN_BUTTON), #вход по кнопке «Войти в аккаунт» на главной
    (urls.main_site_url, Locators.MAIN_LK_BUTTON), #вход через кнопку «Личный кабинет»
    (urls.registration_page_url, Locators.REG_LOGIN_BUTTON), #вход через кнопку в форме регистрации
    (urls.pass_recovery_url, Locators.REG_LOGIN_BUTTON) #вход через кнопку в форме восстановления пароля.
])
def test_login_button_action(url, locator, driver):
    driver.get(url)
    driver.find_element(*locator).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

    current_url = driver.current_url

    assert current_url == urls.login_page_url