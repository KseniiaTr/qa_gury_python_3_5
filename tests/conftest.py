import pytest
from selene.support.shared import browser


@pytest.fixture()
def size_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 1200
    pass

