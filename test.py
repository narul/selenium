from selenium import webdriver
from selenium.webdriver.common.keys import Keys


subject = 'Python'
browser = webdriver.Chrome()
site = "https://www.google.com/"
browser.get(site)
write = browser.find_element_by_name('q')
write.send_keys(subject)
enter = browser.find_element_by_name('q')
enter.send_keys(Keys.RETURN)
for i in range(1, 5):
    selector = '#rso > div:nth-child({}) > div > div.r > a > h3'.format(i)
    link = browser.find_element_by_css_selector(selector)
    print(link.text)
