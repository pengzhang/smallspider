from twitter_crawler.api import get_api
import json

if __name__ == "__main__":
    proxies = {
        # "https": '127.0.0.1:1080',
        # "http": '127.0.0.1:1080'
    }
    api = get_api(proxies)
    # result = api.get_user_timeline(screen_name='pantwtwtw', count=1)
    result = api.get_tweet_comments(post_id="1467435680968105990", count=10000)
    # result = api.get_tweet_info(post_id="1120206463438188544")
    # result = api.get_tweet_info(post_id="1518852739421323265")
    # result = api.get_user_info(screen_name='realllkk520')
    # result = api.get_batch_tweet_info(post_ids=['1417730882090135552'])
    # result = api.get_batch_user_info(user_ids=['1016499781500170240'], screen_names=['bbcchinese'])
    # result = api.search_tweets(keyword="vivo gimbal camera", count=50)
    # result = api.search_users(keyword='vivo camera', count=50)
    # result = api.get_user_followers(screen_name='bbcchinese', count=401)
    # result = api.get_user_followings(screen_name='bbcchinese', count=401)
    # result = api.get_user_list(screen_name='harrytemp2', count=401)
    # result = api.get_conversion(post_id='1521574200183566338')

    print(json.dumps(result, ensure_ascii=False, indent=4))