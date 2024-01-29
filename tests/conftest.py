from pytest import fixture
from config import Config


def pytest_addoption(parser):
    parser.addoption("--env", 
                     action="store",
                     help="Enviroment to run tests against"
                     
    )
    
@fixture(scope='session')
def env(request):
    print("Env is working now")
    return request.config.getoption("--env")

@fixture(scope="session")
def app_config(env):
    print("app_config is working now")
    cfg = Config(env)
    return cfg