from pprint import pprint
import instagram_scraper

args = {"login_user": "peterzh4", "login_pass": "qaz12345678"}

insta_scraper = instagram_scraper.InstagramScraper(**args)
insta_scraper.authenticate_with_login()
shared_data = insta_scraper.get_shared_data_userinfo(username='vencent561215')

arr = []

for item in insta_scraper.query_media_gen(shared_data):
    arr.append(item)

pprint(arr)