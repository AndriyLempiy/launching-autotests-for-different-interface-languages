def test_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert add_button != [], "The 'Add to basket' button is absent!"
