import argparse
from datetime import datetime

from app.handlers import ECommerceCrawler
from app.logger import logger

parser = argparse.ArgumentParser(description="E-Commerce Crawler")
parser.add_argument("--domain_url", help="URL of the domain to extract", default=None)
parser.add_argument("--domain_name", help="Name of the Domain", default=None)
parser.add_argument("--sample", help="Stop the crawler after extracting the goven amount of URLs", default=None)
args = parser.parse_args()

domain_url = args.domain_url
domain_name = args.domain_name
sample = int(args.sample)
logger.info(f"[Crawler | {domain_name}] Started ...")

start = datetime.now()
crawler = ECommerceCrawler(domain_url=domain_url, domain_name=domain_name, sample=sample)
crawler.crawl_all()
end = datetime.now()
logger.info(f"Start: {start}, End: {end}. Time Taken: {end-start}")


# python -m app.app.py --domain_url https://www.nike.com/in/ --domain_name nike
# python -m app.app.py --domain_url https://mamaearth.in/ --domain_name mamaearth