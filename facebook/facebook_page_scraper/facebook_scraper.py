#import Facebook_scraper class from facebook_page_scraper
from facebook_page_scraper import Facebook_scraper
import json
#instantiate the Facebook_scraper class

page_name = "zuck"
posts_count = 10
browser = "firefox"
#proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 600 #600 seconds
headless = True
meta_ai = Facebook_scraper(page_name, posts_count, browser, timeout=timeout, headless=headless)
print('=================')
print(meta_ai.scrap_to_json())