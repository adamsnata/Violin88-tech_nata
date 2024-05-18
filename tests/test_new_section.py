import allure
from resources.new_section import Promo


@allure.title('Test promobanner')
def test_promobanners():
    promo_banners = Promo()

    with allure.step('Open main page'):
        promo_banners.open_main_page()

    with allure.step('Select new_section'):
        promo_banners.select_the_new_section()

    with allure.step('Assert selected new_section'):
        promo_banners.assert_selected_new_section()