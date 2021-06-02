from selenium.webdriver.common.keys import Keys
from Page.BaseApp import BasePage
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_FIELD_IN_IMG = (By.CLASS_NAME, "input__control")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_LISTBOX = (By.CSS_SELECTOR, 'div.mini-suggest__popup')
    LOCATOR_YANDEX_SEARCH_RESULT = (By.CLASS_NAME, "serp-item")
    LOCATOR_YANDEX_SERVICES = (By.CLASS_NAME, "services-new__content")
    LOCATOR_YANDEX_POPULAR_IMAGE = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    LOCATOR_FIRST_IMG = (By.CLASS_NAME, "serp-item__preview")


class SearchHelper(BasePage):
    @allure.step('Ввести слово')
    def enter_word(self, word):
        allure.attach(body="Поиск строки поиска", name="Действие 1", attachment_type=AttachmentType.TEXT)
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        # Проверить наличия поля поиска
        assert search_field is not None, 'Не найдено поле поиска'
        search_field.click()
        allure.attach(body="Набрать слово "+ word, name="Действие 2", attachment_type=AttachmentType.TEXT)
        search_field.send_keys(word)
        return search_field

    @allure.step('Поиск текстового поле')
    def query_text(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD_IN_IMG)
        return search_field

    @allure.step('Нажатие кнопки поиска')
    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    @allure.step('Поиск навбара')
    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    @allure.step('Получение списка подсказок')
    def get_listbox(self):
        search_list = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_LISTBOX)
        assert search_list is not None, 'Не найден выпадающий список'
        return search_list

    @allure.step('Нажать энтер в строке поиске')
    def press_enter_search_field_self(self):
        allure.attach(body="Поиск строки поиска", name="Действие 1", attachment_type=AttachmentType.TEXT)
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        allure.attach(body="Клик в строку поиска", name="Действие 2", attachment_type=AttachmentType.TEXT)
        search_field.click()
        allure.attach(body="Нажать энтер", name="Действие 3", attachment_type=AttachmentType.TEXT)
        search_field.send_keys(Keys.RETURN)

    @allure.step('Проверка результатов')
    def check_search_result(self):
        allure.attach(body="Получение результатов", name="Действие 1", attachment_type=AttachmentType.TEXT)
        search_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULT)
        assert search_list is not None, 'Нет результатов'
        allure.attach(body="Проверка", name="Действие 2", attachment_type=AttachmentType.TEXT)
        is_tensor_here = False
        for i in range(0, 4):
            card_result = search_list[i].find_element(By.TAG_NAME, 'a')
            href = card_result.get_attribute('href')
            sub_ref = "tensor.ru"
            is_tensor_here = href.find(sub_ref)
            if is_tensor_here:
                break
        assert is_tensor_here, 'В первых 5 результатах reference на Тензор не содержится'

    @allure.step('Получение ссылки на сервис Яндекс Картинки')
    def check_images(self):
        allure.attach(body="Поиск сервисов", name="Действие 1", attachment_type=AttachmentType.TEXT)
        search_services = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SERVICES)
        assert search_services is not None, 'Ссылка на сервисы не найдена'
        allure.attach(body="Получение ссылки на картинки", name="Действие 2", attachment_type=AttachmentType.TEXT)
        service = search_services.find_elements(By.CLASS_NAME, 'services-new__list-item')
        images_link = ""
        for i in range(0, len(service)):
            if service[i].find_element(By.TAG_NAME, 'a').get_attribute('data-id') == 'images':
                images_link = service[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
        assert images_link is not None, 'Ссылка на сервис "Картинки" не найдена'
        return images_link

    @allure.step('Получение ссылки на категорию картинок')
    def href_popular_image(self):
        search_category = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_POPULAR_IMAGE).find_element(By.TAG_NAME, 'a').get_attribute('href')
        assert search_category is not None, 'Ссылка на популярные изображения не найдена'
        return search_category

    @allure.step('Получение названия первой категории популярных каритнок')
    def name_of_first_category(self):
        search_category = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_POPULAR_IMAGE)
        name_img_category = search_category.find_element(By.CLASS_NAME, 'PopularRequestList-SearchText').text
        assert name_img_category is not None, 'Название первой категории изображений не найдено'
        return name_img_category

    @allure.step('Получение ссылки на первое изображение')
    def take_first_img_url(self):
        first_img_element = self.find_elements(YandexSearchLocators.LOCATOR_FIRST_IMG)
        href_first_img = first_img_element[0].find_element(By.CLASS_NAME, 'serp-item__link').get_attribute('href')
        assert href_first_img is not None, 'Ссылка на первое изображение не найдена'
        return href_first_img

    @allure.step('Открыть следующую картинку')
    def open_next_img(self):
        arrow_right = self.find_element((By.CLASS_NAME, 'CircleButton_type_next')).find_element(By.CLASS_NAME,
                                                                                                'CircleButton-Icon')
        assert arrow_right is not None, 'Кнопка переключения картинки на следующую не найдена'
        arrow_right.click()

    @allure.step('Открыть предыдущую картинку')
    def open_previous_img(self):
        arrow_left = self.find_element((By.CLASS_NAME, 'CircleButton_type_prev')).find_element(By.CLASS_NAME, 'CircleButton-Icon')
        arrow_left.click()

    def link_format(self,href):
        index = href.find('+')
        while index >= 0:
            href = href.replace('+', r'%20')
            index = href.find('+')
        index = href.find('(')
        while index >= 0:
            href = href.replace('(', r'%28')
            index = href.find('(')
        index = href.find(')')
        while index >= 0:
            href = href.replace(')', r'%29')
            index = href.find(')')
        return href
