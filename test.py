from selenium import webdriver
from selenium.webdriver.common.keys import Keys


name = 'Narul'
browser = webdriver.Chrome()
site = "https://www.google.com/"
browser.get(site)
elem = browser.find_element_by_name('q')
elem.send_keys(name)
elem.send_keys(Keys.RETURN)
for i in range(2, 7):
    selector = '#rso > div:nth-child({}) > div > div.r > a > h3'.format(i)
    link = browser.find_element_by_css_selector(selector)
    print(link.text)
