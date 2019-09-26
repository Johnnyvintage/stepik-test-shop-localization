link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
btn_class_name = "btn-add-to-basket"


class TestShoppingPage():
    def test_presence_add_to_basket_button(self, browser):
        buttons_text = []
        browser.get(link)
        buttons = browser.find_elements_by_class_name(btn_class_name)
        #запись текста из кнопок в массив
        for i in buttons:
            buttons_text.append(i.text)
        #проверка количества найденных кнопок
        assert len(buttons) == 1, f"\nERROR on page {link}: \nThere must be one button \"Add to basket\" (class '{btn_class_name}') on page. Found {len(buttons)}:\n{buttons_text}\n"
