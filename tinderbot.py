from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxProfile
from time import sleep
import random

class Tinderbot:
    def __init__(self):
        self.geo_disabled = FirefoxProfile()
        self.geo_disabled.set_preference("geo.enabled", True)
        self.geo_disabled.set_preference("geo.provider.use_corelocation", True)
        self.geo_disabled.set_preference("geo.prompt.testing", True)
        self.geo_disabled.set_preference("geo.prompt.testing.allow", True)
        self.driver = webdriver.Firefox(executable_path='C:\\Users\\Allen\\OneDrive\\桌面\\geckodriver',firefox_profile=self.geo_disabled)

    def login(self,username,password):
        self.driver.get('https://tinder.com/zh-Hant')
        self.driver.implicitly_wait(10)
        login_button = self.driver.find_element_by_xpath('//*[@id="q-1636318104"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_button.click()
        sleep(5)
        fb_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_button.click()
        base_window = self.driver.window_handles[0]
        pop_window = self.driver.window_handles[1]
        self.driver.switch_to_window(pop_window)
        self.driver.implicitly_wait(10)
        fb_username = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_username.send_keys(username)
        fb_password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_password.send_keys(password)
        fb_password.send_keys(Keys.ENTER)
        self.driver.switch_to_window(base_window)
        sleep(45)
        allow_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        allow_button.click()
        sleep(5)
        no_interest_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        no_interest_button.click()
        cookie_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        cookie_button.click()

    def auto_like(self):
        like_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        dislike_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        the_num = 0
        while True:
            the_num = the_num + 1
            ran_num = random.randint(1,100)
            if ran_num <= 25:
                self.driver.execute_script('arguments[0].click();', dislike_button)
                print(f'{the_num}th: Dislike')
            else:
                self.driver.execute_script('arguments[0].click();', like_button)
                print(f'{the_num}th: Like')
            sleep(3)

    def test_like(self):
        dislike_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        try:
            self.driver.execute_script('arguments[0].click();', dislike_button)
        except:
            print('error')