from pytest import mark


# @mark.skip(reason="broken by deploy somenumber")
@mark.xfail(reason="Env was not QA")
def test_enviroment_is_qa(app_config):
    print("test_env is working now")
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80
    
def test_enviroment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080


# @mark.skip(reason="Not staging enviroment")
# def test_enviroment_is_dev(app_config):
#     base_url = app_config.base_url
#     assert base_url == "staging"