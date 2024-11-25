# shoppin-crawler

### A. Features

-   Simple Crawler to crawl a domain and extract all the product url links in a domain
-   Crawler can be optimized on various parameters

### B. How to run

1. Clone the repo and install requirements:

```
pip install -r requirements.txt
```

2. Change the parameters in app/config.py to optimise the crawling
3. Specify sample arg to test

```
python -m app.app.py --domain_url https://www.nike.com/in/ --domain_name nike --sample 100
```

4. Execute the program and wait for the output with your coffee!

```
python -m app.app.py --domain_url https://www.nike.com/in/ --domain_name nike
```

#####

### C. Future Improvements

-   Add a distributed processing/ async processing library to crawl the domains parallely and extract urls from single domain simultaneously
-   Configure the user agent and figure out the delay between consecutive requests to not get our program recognised as DDOS attack and get blocked
-   Use Database or Shared Cache/ file system to communicate between distributed workers so as to not craw the same url multiple times
-   Product URL discovery can be further improved by applying NLP on html responses. Since all the product pages in e-commerce look similar there will be similarities between their html templates, we can target that
-   Consider adding resume option to save the crawling state perodically for large websites. Will help in resuming the extraction in cases of app crash
-   System to ignore some url paths can be added. Since e-commerce websites contain whole lot of components besides their shop, like reviews, blogs
    which may prove unwarranted in this use case and will increase the depth to be crawled

#### Notes:

-   Sample extraction of 1000 urls can be found in `nike_product_urls.txt`
-   Websites with Infinite scrolling and dynamic content, will require a different strategy. I do not posess deep knowledge of Frontend technologies, but I do understand these cases will have to-be tackled by either simulating the scroll (using slenium etc.) or we will have to identify the API call/ function loading the dynamic content
