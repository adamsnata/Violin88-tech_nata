from selene import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser_management():
   browser.config.base_url = 'https://online.metro-cc.ru/'
   browser.config.window_width = 1600
   browser.config.window_height = 900

   yield

   browser.quit()
