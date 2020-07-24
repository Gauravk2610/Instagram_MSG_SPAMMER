from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Insta_Bot:

    def __init__(self):
        print("WELCOME TO THE INSTAGRAM MESSAGE SPAMMER")
        print("               CODEGRAMMED")
        username = input("Enter Your Instagram Username :- ")
        pw = input("Enter Your Instagram Password :- ")
        self.username = username
        victim_username = input("Enter The Username/Victim To Be Spammed :-  ")
        SPAM_MSG = input("ENTER THE TEXT TO BE SENT :-  ")
        NO = input("ALSO ENTER THE NO. OF MESSAGES TO BE SENT :-  ")        
        self.driver = webdriver.Chrome('Driver/chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://instagram.com')
        sleep(2)
        user_name = self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name.send_keys(username)
        pas = self.driver.find_element_by_xpath('//input[@name="password"]')
        pas.send_keys(pw)
        pas.send_keys(Keys.RETURN)
        notnow = (By.XPATH, "//button[contains(text(), 'Not Now')]")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(notnow)).click()
        notnow = (By.XPATH, '//button[contains(text(), "Not Now")]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(notnow)).click()
        DM = (By.XPATH, '//a[@href="/direct/inbox/"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DM)).click()
        MSG = (By.XPATH, '//button[contains(text(), "Send Message")]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MSG)).click()
        send_msg = (By.XPATH, '//input[@placeholder="Search..."]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(send_msg)).send_keys(victim_username)
        find_id = (By.XPATH, '(//div[contains(text(), "{}")])[1]'.format(victim_username))
        try:
            id_locate = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(find_id))
            print("ID FOUND SUCCESSFULLY")
            id_locate.click()       
        except ElementNotVisibleException:
            print("ID NOT FOUND")
        Next = (By.XPATH, '//div[contains(text(), "Next") ]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Next)).click()
        message = (By.XPATH, '//textarea[@placeholder="Message..."]')
        for i in range(int(NO)):
            SPAM = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(message))
            SPAM.send_keys(SPAM_MSG)
            SPAM.send_keys(Keys.RETURN)
        sleep(10)
        self.driver.close()
Insta_Bot()