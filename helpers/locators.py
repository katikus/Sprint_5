from selenium.webdriver.common.by import By


class Locators:
    REG_NAME_FIELD = (By.XPATH, ".//fieldset[1]//input") # поле ввода имени при регистрации
    REG_EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input") # поле ввода почты при регистрации
    REG_PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]//input") # поле ввода пароля при регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//button[(text() = 'Зарегистрироваться')]") # кнопка "Зарегистрироваться

    LOGIN_BUTTON = (By.XPATH, ".//button[(text() = 'Войти')]") # кнопка "Войти" на странице входа
    LOGIN_PAGE_EMAIL_FIELD = (By.XPATH, ".//input[@name = 'name']") # поле логина на странице входа
    LOGIN_PAGE_PASS_FIELD = (By.XPATH, ".//input[@name = 'Пароль']") # поле пароля на странице входа
    REG_LOGIN_BUTTON = (By.LINK_TEXT, "Войти")  # кнопка "Войти" на странице входа
    REGISTRATION_INCORRECT_PASSWORD_LABEL = (By.XPATH, "//*[contains(@class, 'input__error')]") # Лейбл ошибки ввода пароля

    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[(text() = 'Войти в аккаунт')]") # Кнопка "Войти в аккаунт" на главной странице
    CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")  # Кнопка "Конструктор" на главной странице
    MAIN_LK_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Кнопка "Личный Кабинет" на главной странице
    LOGO = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]" ) #Логотип на главной странице
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[(text() = 'Оформить заказ')]") # кнопка "Оформить заказ" на главной странице

    LK_SAVE_BUTTON = (By.XPATH, ".//button[(text() = 'Сохранить')]") # кнопка "Сохранить" на странице ЛК
    LK_LOGOUT = (By.XPATH, ".//button[(text() = 'Выход')]") # кнопка "Выход" на странице ЛК

    MAIN_TOPPING_BUTTON = (By.XPATH, "//span[(text() = 'Начинки')]/parent::div") # кнопка "Начинки" на странице конструктора
    MAIN_SAUCES_BUTTON = (By.XPATH, "//span[(text() = 'Соусы')]/parent::div") # кнопка "Соусы" на странице конструктора
    MAIN_BUNS_BUTTON = (By.XPATH, "//span[(text() = 'Булки')]/parent::div") # кнопка "Булки" на странице конструктора

    MAIN_BIO_KOTLETA = (By.XPATH, "//p[(text() = 'Хрустящие минеральные кольца')]") # ингридиент "Хрустящие минеральные кольца" на странице конструктора
    MAIN_KRATORS_BUNS = (By.XPATH, "//p[(text() = 'Краторная булка N-200i')]") # ингридиент 'Краторная булка N-200i' на странице конструктора
    MAIN_SAUCE = (By.XPATH, "//p[(text() = 'Соус с шипами Антарианского плоскоходца')]") # ингридиент 'Соус с шипами Антарианского плоскоходца' на странице конструктора