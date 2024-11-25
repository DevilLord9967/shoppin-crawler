from datetime import datetime

from app.handlers import ECommerceCrawler
from app.logger import logger

start = datetime.now()
nike_crawler = ECommerceCrawler(domain_url="https://www.nike.com/in/", domain_name="nike")
nike_crawler.crawl_all()
end = datetime.now()
logger.info(f"Start: {start}, End: {end}. Time Taken: {end-start}")
