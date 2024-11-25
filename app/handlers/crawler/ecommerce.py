from pprint import pformat
import time
from typing import List

from app.config import app_config
from app.logger import logger

from ..parser import URLParser
from .url import URLCrawler


class ECommerceCrawler:
    def __init__(self, domain_url: str, domain_name: str) -> None:
        self.domain_url = domain_url
        self.domain_name = domain_name
        self.visited_urls = set()
        self.product_urls = set()
        self.urls_to_visit = []
        self.url_parser = URLParser(url_patterns=app_config.PRODUCT_URL_PATTERNS)
        self.logger_prefix = f"[Crawler | {self.domain_name}] "
        self._initial_crawl()

    def _initial_crawl(self):
        linked_urls = URLCrawler(url=self.domain_url).crawl()
        for url in linked_urls:
            if self.url_parser.is_product_url(url_path=url):
                self.product_urls.add(url)
        self.urls_to_visit.extend(linked_urls)

    def crawl_once(self) -> str:
        # TODO: Optimization, Crawl the following url in async task manager (like celery)
        url_to_crawl = self.urls_to_visit.pop(0)
        logger.info(self.logger_prefix + f"Crawling: {url_to_crawl}")
        linked_urls = URLCrawler(url=url_to_crawl).crawl()
        for url in linked_urls:
            if self.url_parser.is_product_url(url_path=url):
                self.product_urls.add(url)
                logger.info(self.logger_prefix + f"Product URL Found: {url}")
            if url in self.visited_urls:
                continue
            else:
                self.urls_to_visit.append(url)
        return url_to_crawl

    def crawl_all(self):
        while self.urls_to_visit:
            url = self.urls_to_visit[0]
            try:
                url = self.crawl_once()
                time.sleep(app_config.URL_CRAWL_BUFFER)
            except:
                logger.error(self.logger_prefix + f"Crawling Failed: {url}")
        file_name = f"{self.domain_name}_product_urls.txt"
        with open(file_name, "w") as f:
            f.write(pformat(self.product_urls))
        logger.info("\n\n" + self.logger_prefix + f"Product URLs written to file: {file_name}")
