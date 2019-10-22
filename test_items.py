link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_can_add_product_to_basket(browser):
    browser.get(link)
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button != 0
