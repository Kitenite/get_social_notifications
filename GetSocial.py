from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def startChrome():
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=/Users/kietho/Library/Application\ Support/Google/Chrome/Default")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    return driver

def get_facebook(driver):
    print("Facebook:")
    url = 'https://www.facebook.com'
    driver.get(url)
    els = driver.find_elements(By.XPATH, "//*[contains(@aria-label, 'unread')]")
    notifications = set()
    for el in els:
        notifications.add(el.get_attribute('aria-label'))
    
    if notifications:
        print(f"\t{len(notifications)} notifications found:")
        for notif in notifications:
            print(f"\t \t{notif}")
    else:
        print("\tNo unread notifications")

def get_linkedin(driver):
    print("LinkedIn:")
    url = 'https://www.linkedin.com/feed/'
    driver.get(url)
    els = driver.find_elements(By.XPATH, "//*[contains(@aria-label, 'unread')]")
    notifications = set()
    for el in els:
        notifications.add(el.get_attribute('aria-label'))
    
    if notifications:
        print(f"\t{len(notifications)} notifications found:")
        for notif in notifications:
            print(f"\t \t{notif}")
    else:
        print("\tNo unread notifications")

def get_instagram(driver):
    print("Instagram:")
    url = 'https://www.instagram.com/accounts/activity/'
    driver.get(url)
    time.sleep(5)

    els = driver.find_elements(By.XPATH, "//*[text()='New']")
    if els:
        print("\tNew notifications found")
    else:
        print("\tNo unread notifications")

if __name__ == "__main__":
    driver = startChrome()
    get_facebook(driver)
    get_linkedin(driver)
    get_instagram(driver)
