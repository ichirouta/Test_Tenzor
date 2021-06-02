import allure
from Yandex.YandexPages import SearchHelper


@allure.id('1')
@allure.title('Поиск в яндексе')
@allure.story('Ищем в яндексе')
def test_yandex_search(browser):
    # Зайти на yandex.ru
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    # Ввести в поиск Тензор
    yandex_main_page.enter_word("Тензор")
    # Проверить, что появилась таблица с подсказкам
    yandex_main_page.get_listbox()
    # При нажатии Enter появляется таблица результатов поиск
    yandex_main_page.press_enter_search_field_self()
    # В первых 5 результатах есть ссылка на tensor.ru
    yandex_main_page.check_search_result()
