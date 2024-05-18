from selene import browser, have

class Promo:
    def open_main_page(self):
        browser.open('/')

    def select_the_new_section(self):
        browser.element(
            '.header-categories__item:nth-child(1) > .header-categories__item-link'
        ).click()

    def assert_selected_new_section(self):
        browser.element('.subcategory-or-type__heading-title').should(
            have.text('Новинки в METRO'))

