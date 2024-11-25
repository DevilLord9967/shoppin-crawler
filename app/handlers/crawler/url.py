from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class URLCrawler:
    def __init__(self, url: str):
        self.url = url

    def download_url(self) -> str:
        # TODO: Optimization, Make this function async
        return requests.get(self.url).text

    def get_linked_urls(self, html) -> set:
        soup = BeautifulSoup(html, "html.parser")
        linked_urls = set()
        for link in soup.find_all("a"):
            path = link.get("href")
            if path and path.startswith("/"):
                path = urljoin(self.url, path)
            linked_urls.add(path)
        return linked_urls

    def crawl(self) -> set:
        html = self.download_url()
        linked_urls = self.get_linked_urls(html)
        return linked_urls
