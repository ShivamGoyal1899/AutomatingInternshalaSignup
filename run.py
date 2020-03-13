from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from getpass import getpass
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

for i in range(0, 1000):
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)
    driver.get('https://internshala.com/fake_page?utm_source=refer_copylink&utm_medium=fake_utm')
    time.sleep(2)

    driver.find_element_by_id('email').send_keys('fake_uname'+str(i)+'@fake_dns.fake_tld')
    time.sleep(1)

    driver.find_element_by_id('password').send_keys('fake_pwd')
    time.sleep(1)

    driver.find_element_by_id('first_name').send_keys('fake_fname')
    time.sleep(1)

    driver.find_element_by_id('last_name').send_keys('fake_lname')
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="registration-form"]/button').click()
    time.sleep(5)

    print('YaY! User {} has been registered.'.format(i))
    driver.close()