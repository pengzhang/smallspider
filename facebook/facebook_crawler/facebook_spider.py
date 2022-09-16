from facebook_scraper import get_posts

for post in get_posts('zuck', cookies="cookies.txt", pages=10):
    print(post)
    #print(post['text'][:50])
