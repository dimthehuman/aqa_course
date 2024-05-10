from selenium import webdriver


def driver_factory(browser_name: str):
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        return webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(options=options)
