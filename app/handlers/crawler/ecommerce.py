from pprint import pformat
import time
from typing import List

from app.config import app_config
from app.logger import logger

from ..parser import URLParser
from .url import URLCrawler


class ECommerceCrawler:
    def __init__(self, domain_url: str, domain_name: str, sample: int = None) -> None:
        self.domain_url = domain_url
        self.domain_name = domain_name
        self.sample = sample
        self.visited_urls = set()
        self.product_urls = set()
        self.urls_to_visit = []
        self.url_parser = URLParser(url_patterns=app_config.PRODUCT_URL_PATTERNS)
        self.logger_prefix = f"[Crawler | {self.domain_name}] "
        self.crawl_once(domain_url)

    # def _initial_crawl(self):
    #     linked_urls = URLCrawler(url=self.domain_url).crawl()
    #     for url in linked_urls:
    #         if self.url_parser.is_product_url(url_path=url):
    #             self.product_urls.add(url)
    #     self.urls_to_visit.extend(linked_urls)

    def crawl_once(self, url_to_crawl: str) -> str:
        # TODO: Optimization, Crawl the following url in async task manager (like celery)
        logger.info(self.logger_prefix + f"Crawling: {url_to_crawl}")
        linked_urls = URLCrawler(url=url_to_crawl).crawl()
        # self.visited_urls.add(url_to_crawl)
        for url in linked_urls:
            if app_config.ONLY_CRAWL_DOMAIN and not url.startswith(self.domain_url):
                #* Prevents redirect to other domains
                #* Helps in crawling a subset of domain
                continue
            if self.url_parser.is_product_url(url_path=url) and url not in self.product_urls:
                self.product_urls.add(url)
                logger.info(self.logger_prefix + f"Product URL Found: {url}")
            if url in self.visited_urls or url in self.urls_to_visit:
                continue
            else:
                self.urls_to_visit.append(url)

    def crawl_all(self):
        while self.urls_to_visit:
            url_to_crawl = self.urls_to_visit.pop(0)
            try:
                if url_to_crawl not in self.visited_urls:
                    self.crawl_once(url_to_crawl)
                time.sleep(app_config.URL_CRAWL_BUFFER)
            except:
                logger.exception(self.logger_prefix + f"Crawling Failed: {url_to_crawl}")
            finally:
                self.visited_urls.add(url_to_crawl)
                
            if self.sample is not None and len(self.product_urls) >= self.sample:
                break
        file_name = f"{self.domain_name}_product_urls.txt"
        with open(file_name, "w") as f:
            f.write(pformat(self.product_urls))
        logger.info("\n\n" + self.logger_prefix + f"Product URLs written to file: {file_name}")
