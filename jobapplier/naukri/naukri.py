import os

import selenium
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NaukriController:
    def __init__(self, config):
        self.config = config
        self.driver = wb.Chrome()
        self.skillset = ['Analysis', 'Python', 'SQL']
        self.LL = config.job_preferences.minimum_lpa
        self.UL = config.job_preferences.maximum_lpa
        self.location = config.job_preferences.location.lower().replace(" ", "-")
        self.role = config.job_preferences.role.lower().replace(" ", "-")

    def login(self):
        self.driver.get(self.config.naukri.url)
        self.driver.find_element(By.XPATH,'//*[@id="login_Layer"]/div').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/form/div[2]/input').send_keys(
            self.config.naukri.username)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/form/div[3]/input').send_keys(
            self.config.naukri.password)
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/form/div[6]/button').click()
        for i in range(1, 6):
            self.driver.get('https://www.naukri.com/' + self.role + '-jobs-in-' + self.location + '-' + str(i) + '?ctcFilter=' + str(
                self.LL) + 'to' + str(self.UL))
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            self.driver.get(url)
            try:
                test = self.driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[2]')
                if all(word in test.text.lower() for word in self.skillset):
                    self.driver.find_element_by_xpath(
                        '//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]').click()
                    time.sleep(2)
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                else:
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
            except Exception as e:
                print(e)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
    def apply(self):
        self.login()
        print(self.config)
        print(self.config.driver)
