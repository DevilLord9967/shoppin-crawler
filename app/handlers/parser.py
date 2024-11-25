import re
from typing import List


class URLParser:
    def __init__(self, url_patterns: List[str]) -> None:
        self.url_patterns = url_patterns

    def is_product_url(self, url_path: str):
        for url_pattern in self.url_patterns:
            match_result = re.search(url_pattern, string=url_path)
            if match_result is not None:
                return True
        return False
