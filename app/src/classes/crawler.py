from bs4 import BeautifulSoup
import requests

class Crawler:
    def __init__(self, name: str, link: str):
        self.name: str = name
        self.link: str = link

        self.web_page = requests.get(link)

        self.soup = BeautifulSoup(self.web_page.text, 'html.parser')

        latest_release = self.soup.find("li", class_="p-list__item")
        latest_release_link = latest_release.find("a").get("href")

        self.web_page_second = requests.get(self.link+latest_release_link)
        self.soup_second = BeautifulSoup(self.web_page_second.text, 'html.parser')

        iso_block = self.soup_second.find_all("div", class_="col-6 p-divider__block")
        iso_link = iso_block[1].find("a").get("href")

        self.full_link = self.link+latest_release_link+iso_link
        print(self.full_link)

