import allure
from resources.find_product_page import Product

@allure.title('Find product')
def test_find_product():
    product = Product()

    with allure.step('Open main page'):
        product.open_main_page()

    with allure.step('Enter the product name'):
        product.search_product('METRO Chef Мороженое Пломбир ванильный, 2.5кг')

    with allure.step('Add to cart'):
        product.add_to_cart()

    with allure.step('choose_delivery_method'):
        product.choose_manual_receipt()

    with allure.step('change_city'):
        product.change_city()

    with allure.step('choose city'):
        product.choose_city('Ульяновск')

    with allure.step('confirm city'):
        product.confirm_city()

    with allure.step('click button change'):
        product.click_button()

    with allure.step('click to the cart'):
        product.click_to_the_cart()

    with allure.step('assert sum'):
        product.assert_product()