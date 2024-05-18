from selene import browser, have, be, by

class Delete:
    def open_main_page(self):
        browser.open('/')

    def search_product(self, value):
        browser.element('[data-qa=header-search-input]').should(be.blank).type(
            value
        ).press_enter()

    def add_to_cart(self):
        browser.element('.product-card__content .simple-button__text').click()

    def choose_manual_receipt(self):
        browser.element('.delivery__tab:nth-child(2)').click()

    def change_city(self):
        browser.element('.pickup-content__city > .reset-link').click()

    def choose_city(self, value):
        browser.element('.style--popup-change-tradecenter .base-input__input-field').click(). \
            type('Ульяновск').press_enter()

    def confirm_city(self):
        browser.element('[class="city-item"]').click()

    def click_button(self):
        browser.element('.delivery__btn-apply').click()

    def click_to_the_cart(self):
        browser.element('[data-qa=header-cart-button]').press_enter()

    def remove_product(self):
        browser.element('[class~=button-remove]').click()

    def assert_empty(self):
        browser.element('[class="header-cart-empty__title"]').should(have.text('В корзине пусто'))