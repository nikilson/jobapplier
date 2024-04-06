import selenium
from selenium import webdriver as wb
import pandas as pd
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class NaukriController:
    def __init__(self, config):
        self.config = config
        self.driver = wb.Chrome(config.driver)

    def apply(self):
        print(self.config)
