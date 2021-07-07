from selenium import webdriver


def browse(url):
    driver = webdriver.Chrome()
    driver.get(url)


def close():
    driver = webdriver.Chrome()
    driver.close()
