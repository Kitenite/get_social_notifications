from platform import platform
from bs4 import BeautifulSoup
import requests
import json
import time
from pycookiecheat import chrome_cookies


"""
Entry
Get credentials
Sign in for each link
Get HTML

class getsocial
    init
        give creds object

    get notifications for each platform based on object
        use scraper for helpers

"""

cred_path = "/Users/kietho/Repos/fun/GetNotifications/credentials.json" 

class SocialManager():
    platforms = None

    def __init__(self, cred_path):
        self.platforms = self.json_to_obj(cred_path)
        # Infer link if none are provided 
        for key in self.platforms:
            if "link" not in  self.platforms[key]:
                self.platforms[key]["link"] = f"https://www.{key}.com/"         

    def json_to_obj(self, filename):
        # Helper to extract data from JSON file
        obj = None
        with open(filename) as json_file:
            obj = json.loads(json_file.read())
        return obj

    def get_notifications(self):
        for key in self.platforms:
            url = self.platforms[key]['notification_link']
            soup = self.get_soup_using_cookies(url)
            print(f"Getting notification for {key}:")
            # parse notifications
            # if key == 'facebook':
            #     self.parse_facebook(soup)
            # elif key == 'instagram':
            #     self.parse_instagram(soup)
            if key == 'linkedin':
                self.parse_linkedin(soup)
            # else:
            #     print(f"Unknown key for platform: {key}")

    def parse_facebook(self, soup):
        notification_list = soup.find("div", {"id": "notifications_list"})
        print(notification_list)

    def parse_instagram(self, soup):
        print(soup.prettify())

            
    def parse_linkedin(self, soup):
        # print(soup.prettify())
        print(soup.findAll('a'))
        for a in soup.find_all('a', href="/accounts/activity/"):
            print(a)

    def get_soup_using_cookies(self, url):
        s = requests.Session()
        cookies = chrome_cookies(url)
        response = s.get(url, cookies = cookies)
        return BeautifulSoup(response.text, 'html.parser')

# def get_by_tag(url):
#     soup = BeautifulSoup(get_html(url), 'html.parser')
#     print(soup.prettify())
#     tags=soup.findAll('img')
#     clr_img_urls = [tag['src'].strip() for tag in tags]
#     return clr_img_urls



if __name__ == '__main__':
    credManager = SocialManager(cred_path)
    credManager.get_notifications()