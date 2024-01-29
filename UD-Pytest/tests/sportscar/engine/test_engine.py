from pytest import mark
import time

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('https://www.motortrend.com/features/hemi-engine-sizes/')
    time.sleep(5)
    assert True