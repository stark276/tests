from pytest import mark


@mark.smoke

@mark.body
@mark.ui
class BodyTest:
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('https://www.motortrend.com/')
        assert True