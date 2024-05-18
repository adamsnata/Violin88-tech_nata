import allure
from resources.catalog_page import Catalog

@allure.title('Catalog')
def test_catalog_section():
    catalog_section = Catalog()

    with allure.step('Open main page'):
        catalog_section.open_main_page()

    with allure.step('Open catalog section'):
        catalog_section.open_catalog()

    with allure.step('Select_of_position'):
        catalog_section.select_the_catalog_position()

    with allure.step('Assert catalog section'):
        catalog_section.assert_catalog_section()

