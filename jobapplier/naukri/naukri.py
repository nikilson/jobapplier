from selenium import webdriver as wb

import time
from selenium.webdriver.common.by import By


class NaukriController:
    def __init__(self, config, limit, mode):
        self.config = config
        self.driver = wb.Chrome()
        self.skill_sets = config.job_preferences.skill_sets
        self.LL = config.job_preferences.minimum_lpa
        self.UL = config.job_preferences.maximum_lpa
        self.location = config.job_preferences.location.lower().replace(" ", "-")
        self.role = config.job_preferences.role.lower().replace(" ", "-")
        self.job_urls = []
        self.limit = int(limit)
        self.mode = mode

    def login(self):
        self.driver.get(self.config.naukri.url)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="login_Layer"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input').send_keys(
            self.config.naukri.username)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input').send_keys(
            self.config.naukri.password)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button').click()

    def search_jobs(self):
        i = 0
        while self.limit > len(self.job_urls):
            i += 1
            search_url = f"{self.config.naukri.url}{self.role}-jobs-in-{self.location}-{i}?ctcFilter={self.LL}to{self.UL}"
            print(search_url)
            self.driver.get(search_url)
            # WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            # self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            self.driver.get(url)
            time.sleep(5)
            container = self.driver.find_elements(By.TAG_NAME, 'a')
            for item in container:
                href = item.get_attribute("href")
                if href and href.startswith("https://www.naukri.com/job-listings-"):
                    self.job_urls.append(href)

    def apply_jobs(self):
        job_applied = 0
        for job in self.job_urls:
            try:
                self.driver.get(job)
                time.sleep(5)
                if self.mode == "auto":
                    self.driver.find_element(By.XPATH, '//*[@id="apply-button"]').click()
                else:
                    time.sleep(15)
                job_applied += 1
                time.sleep(2)
            except Exception as e:
                print(f"ERROR: Couldn't apply for the job:{job[-1:-12]}")

        print(f"LOG: Number of Job applied: {job_applied}")

    def apply(self):
        self.login()
        self.search_jobs()
        self.apply_jobs()
