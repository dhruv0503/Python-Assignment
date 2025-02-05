import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

recipient = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')
id_elem = browser.find_element_by_name('identifier')
id_elem.send_keys('email@gmail.com')
id_elem.send_keys(Keys.ENTER)
time.sleep(3)

pass_elem = browser.find_element_by_name('password')
pass_elem.send_keys('password')
pass_elem.send_keys(Keys.ENTER)
time.sleep(5)

compose_elem = browser.find_element_by_class_name('z0')
compose_elem.click()
time.sleep(5)

to_elem = browser.find_element_by_name('to')
to_elem.send_keys(recipient)

subject_elem = browser.find_element_by_name('subjectbox')
subject_elem.send_keys(subject)

subject_elem.send_keys(Keys.TAB + message + Keys.TAB + Keys.ENTER)
time.sleep(5)

browser.quit()