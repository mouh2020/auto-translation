from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
options=Options()
options.headless=True
class Chrome():
    @staticmethod
    def translation_url(from_lang,to_lang):
        url = 'https://translate.google.com/?sl=(from)&tl=(to)&op=translate'
        url=url.replace('(from)',from_lang)
        url = url.replace('(to)', to_lang)
        return url    ######################### Return Translation URL
    @staticmethod
    def translation_text_url(text,from_lang,to_lang):
        url = Chrome.translation_url(from_lang, to_lang)
        text = text.replace(' ', '%20')
        url = url.replace('op', 'text=' + text + '&op')
        return url    ########################## Return Url Of The Translation Text
    @staticmethod
    def translate_text(text,from_lang,to_lang):
        driver = webdriver.Chrome(options=options)
        driver.get(Chrome.translation_text_url(str(text), from_lang, to_lang))
        return_translation = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span'
        translation=str(driver.find_element_by_xpath(return_translation).text)
        driver.close()
        return translation
    @staticmethod
    def text_2_speech(text, language):
        driver = webdriver.Chrome(options=options)
        driver.set_window_position(-10000, 0)
        driver.get(Chrome.translation_text_url(str(text), from_lang=language, to_lang='fr'))
        audio_button = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/div[5]/div[1]/div/div[2]/div/span/button'
        driver.find_element_by_xpath(audio_button).click()
        count = 0
        for i in range(1000000000):
            time.sleep(0.1)
            if not(str(driver.find_element_by_xpath(audio_button).text)) == 'volume_up':
                count += 1
            else:
                driver.close()
                break
    @staticmethod
    def translation_2_speech(text,from_lang,to_lang):
        driver = webdriver.Chrome(options=options)
        driver.get(Chrome.translation_text_url(str(text), from_lang, to_lang))
        audio_button_translation = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[4]/div[1]/div[2]/div/span/button'
        driver.find_element_by_xpath(audio_button_translation).click()
        count = 0
        for i in range(100000000):
            time.sleep(0.1)
            if str(driver.find_element_by_xpath(audio_button_translation).text) == 'stop':
                count += 1
            else:
                driver.close()
                break