import time
from Yandex.YandexPages import SearchHelper
import allure
from allure_commons.types import AttachmentType


@allure.id('2')
@allure.title('Картинки на яндексе')
@allure.story('Открываем главную страницу яндекса, проверяем работоспособность сервиса яндекс картинки')
def test_yandex_Picture(browser):
    # Зайти на yandex.ru
    yandex_page = SearchHelper(browser)
    yandex_page.go_to_site()
    # Ссылка «Картинки» присутствует на странице
    href = yandex_page.check_images()
    # Кликаем на ссылку
    yandex_page.driver.get(href)
    assert yandex_page.driver.current_url == href is not None, 'URL не соответствует'
    # Открыть 1 картинку
    name_category_before_opening = yandex_page.name_of_first_category()
    href = yandex_page.href_popular_image()
    yandex_page.driver.get(href)
    # Проверить что открылась
    assert yandex_page.driver.current_url == href is not None, 'URL не соответствует'
    # В поиске верный текст
    name_category_in_search_field = yandex_page.query_text().get_attribute('value')
    assert name_category_in_search_field == name_category_before_opening, 'Текст в поиске неверный'
    # Открыть 1 картинку
    href = yandex_page.take_first_img_url()
    yandex_page.driver.get(href)
    # Проверить что открылась
    # Работа со ссылой
    href = yandex_page.link_format(href)
    assert yandex_page.driver.current_url == href is not None, 'URL открывшейся картинки не соответствует'
    time.sleep(0.2)  # Задержка
    href = yandex_page.driver.current_url
    # При нажатии кнопки вперед картинка изменяется
    yandex_page.open_next_img()
    # При нажатии кнопки назад картинка изменяется
    yandex_page.open_previous_img()
    time.sleep(0.2)  # Задержка
    assert yandex_page.driver.current_url == href is not None, 'Открылось не прошлое изображение'
    allure.attach(yandex_page.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

