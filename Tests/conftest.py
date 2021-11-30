import pytest
import selenium.webdriver



def pytest_addoption(parser):
  parser.addoption('--browser', action='store', default='chrome',
                    help ='setup browser: Chrome')

@pytest.fixture
def browser(request):
  sel_browser = request.config.getoption("--browser")

  if sel_browser == 'chrome':
    b = selenium.webdriver.Chrome()
  else:
    raise Exception(f'Browser '+sel_browser+'  is not supported')

  b.implicitly_wait('20')
  yield b
  b.quit()










"""
@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

@pytest.fixture
def browser(config):

    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()

"""
