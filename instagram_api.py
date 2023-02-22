from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
from time import sleep


class Instagram:
    def __init__(self) -> None:
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument('--lang=en-US')

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://www.instagram.com/')

    def login(self, login: str, password: str):
        cookie_prompt = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//button[text()="Only allow essential cookies"]')))
        cookie_prompt.click()

        login_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
        login_input.send_keys(login)
        password_input.send_keys(password)
        submit_button.click()

        save_login_prompt = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(text(), "Not Now")]')))
        save_login_prompt.click()

        notifications_prompt = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(text(), "Not Now")]')))
        notifications_prompt.click()

    def upload(self, image_path: str):
        upload = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a')))
        upload.click()

        select_from_computer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Select from computer")]')))
        select_from_computer.click()

        sleep(1)
        pyautogui.write(image_path)
        sleep(1)
        pyautogui.press('enter')

        for x in range(2):
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Next")]')))
            next_button.click()
            sleep(1)

        share_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Share")]')))
        share_button.click()

        sleep(5)
        close_upload = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_Fj"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div')))
        close_upload.click()
