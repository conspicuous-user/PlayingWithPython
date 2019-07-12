from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import constants
import word_generator
import time
import random

class TwitterCrawler:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.crawl = webdriver.Firefox()

    def login(self):
        crawl = self.crawl
        crawl.get('https://twitter.com')
        time.sleep(random.randint(2, 7))
        email = crawl.find_element_by_class_name('email-input')
        passw = crawl.find_element_by_name('session[password]')
        email.clear()
        passw.clear()

        email.send_keys(self.email)
        passw.send_keys(self.password)
        time.sleep(random.randint(2, 7))
        passw.send_keys(Keys.RETURN)
        time.sleep(random.randint(2, 7))

    def make_friends(self, tags):
        crawl = self.crawl
        crawl.get('https://twitter.com/search?q=' + tags + '&src=typd')
        time.sleep(3)

        for i in range(1, random.randint(2, 6)):
            crawl.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(random.randint(2, 7))
            tweets = crawl.find_elements_by_class_name('tweet')
            hyperlink = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(len(hyperlink))

            i = 1
            for link in hyperlink:
                try:
                    print(str(i) + '/' + str(len(hyperlink)) + ' ' + link)
                    crawl.get('https://twitter.com' + link)
                    crawl.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(random.randint(5, 23))
                except Exception as e:
                    time.sleep(random.randint(1, 20))
                i += 1
        time.sleep(random.randint(1, 4))
        self.crawl.close()


while True:
    hashtag = word_generator.random_tag_generator()
    space_cat = TwitterCrawler(constants.username, constants.password)
    space_cat.login()
    space_cat.make_friends(hashtag)
