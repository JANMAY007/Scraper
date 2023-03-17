import re
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def initialize(email, password, browser):
    try:
        email_element = browser.find_element("id", "session_key")
        email_element.send_keys(email)
        pass_element = browser.find_element("id", "session_password")
        pass_element.send_keys(password)
        pass_element.submit()
        print("success! Logged in")
        time.sleep(3)
        return True
    except TimeoutError:
        print("Failed to login")
        browser.close()
        return False

def url_scraper(email, password, url):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.linkedin.com")
    browser.maximize_window()
    time.sleep(2)
    if initialize(email, password, browser):
        browser.get(url)
        time.sleep(2)
        contact_page = BeautifulSoup(browser.page_source, features="html.parser")
        time.sleep(2)
        try:
            phone_contact_page = contact_page.findAll(attrs={'class': re.compile(r"^t-14 t-black t-normal$")})
            fetch_phone = phone_contact_page[0].text
        except IndexError:
            fetch_phone = 0000
        content_contact_page = contact_page.find_all('a', href=re.compile("mailto"))
        fetch_email = ''
        for contact in content_contact_page:
            fetch_email += contact.get('href')[7:]
        browser.close()
        return [fetch_email, fetch_phone]

def bulk_url_scraper(email, password, urls):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.linkedin.com")
    browser.maximize_window()
    time.sleep(2)
    if initialize(email, password, browser):
        data = []
        for url in urls:
            browser.get(url)
            time.sleep(2)
            contact_page = BeautifulSoup(browser.page_source, features="html.parser")
            time.sleep(2)
            try:
                phone_contact_page = contact_page.findAll(attrs={'class': re.compile(r"^t-14 t-black t-normal$")})
                fetch_phone = phone_contact_page[0].text
            except IndexError:
                fetch_phone = 0000
            content_contact_page = contact_page.find_all('a', href=re.compile("mailto"))
            fetch_email = ''
            for contact in content_contact_page:
                fetch_email += contact.get('href')[7:]
            data.append([fetch_email, fetch_phone])
        browser.close()
        return data
