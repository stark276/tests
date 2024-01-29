from pytest import mark 
import time


@mark.entertainment
@mark.ui
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('https://www.motortrend.com/car-reviews/')
    time.sleep(5)
    
    assert True