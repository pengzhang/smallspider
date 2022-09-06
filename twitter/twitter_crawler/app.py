from flask import Flask
from twitter_crawler.api import get_api
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/twitter")
def twitter():
    api = get_api({})
    result = api.get_user_timeline(screen_name='pantwtwtw', count=1)
    # result = api.get_tweet_comments(post_id="1467435680968105990", count=10000)
    return json.dumps(result, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

#gunicorn -w 4 -b 0.0.0.0:8081 -D app:app  