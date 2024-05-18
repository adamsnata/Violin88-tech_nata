import allure
from resources.delete_product import Delete

@allure.title('Remove product')
def test_find_product():
    delete = Delete()

    with allure.step('Open main page'):
        delete.open_main_page()

    with allure.step('Enter the product name'):
        delete.search_product('METRO Chef Мороженое Пломбир ванильный, 2.5кг')

    with allure.step('Add to cart'):
        delete.add_to_cart()

    with allure.step('choose_delivery_method'):
        delete.choose_manual_receipt()

    with allure.step('change_city'):
        delete.change_city()

    with allure.step('choose city'):
        delete.choose_city('Ульяновск')

    with allure.step('confirm city'):
        delete.confirm_city()

    with allure.step('click button change'):
        delete.click_button()

    with allure.step('click to the cart'):
        delete.click_to_the_cart()

    with allure.step('Remove product'):
        delete.remove_product()

    with allure.step('The cart empty'):
        delete.assert_empty()

