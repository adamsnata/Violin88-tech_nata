from selene import browser, have
browser.config.timeout = 5

class Catalog:

    def open_main_page(self):
        browser.open('/')

    def open_catalog(self):
        browser.element('[data-qa=header-catalog-button]').click()

    def select_the_catalog_position(self):
        browser.element('li:nth-child(7) span:nth-child(2)').click()

    def assert_catalog_section(self):
        browser.element(
            ".slider-main-block__heading--h1 .slider-main-block__heading-title"
        ).should(have.text('Чай, кофе, какао'))

