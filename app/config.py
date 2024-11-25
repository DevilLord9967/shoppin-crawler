from typing import List
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_ENV: str = "DEV"
    
    #* Configuration to optimize the crawler
    URL_CRAWL_BUFFER: float = 0.4 # seconds
    PRODUCT_URL_PATTERNS: List[str] = [".\/t\/."]
    
    #TODO: Future Consideration
    CONCURRENT_REQUESTS: int = 1


app_config = AppSettings()
