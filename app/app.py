from app.handlers import ECommerceCrawler

nike_crawler = ECommerceCrawler(domain_url="https://www.nike.com/", domain_name="nike")
nike_crawler.crawl_all()