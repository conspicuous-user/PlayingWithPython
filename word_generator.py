from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def random_tag_generator():
    crawl = webdriver.Firefox()
    crawl.get('https://wordcounter.net/random-word-generator')

    # set to one word
    time.sleep(3)
    number_input_box = crawl.find_element_by_id('random_words_count')
    number_input_box.clear()
    number_input_box.send_keys('1')
    time.sleep(2)

    # click generate random words
    crawl.find_element_by_id('random-words').click()
    time.sleep(2)

    # get word from random generation
    word = crawl.find_element_by_class_name('random_word')
    random_word = word.get_attribute("innerHTML")
    print(random_word)
    time.sleep(1)
    crawl.close()
    return random_word
