import csv

import tweepy  # To consume Twitter's API
import pandas as pd
import preprocessor as p
import re
import string
import json
import pymongo

# client = pymongo.MongoClient("mongodb://dhruvesh:root@18.216.165.78/assigndb")
# db = client.assigndb
# collection = db['news']

# credentials
consumer_key = 'Ap3f7BSkmIyqI84ePYCXtluq4'
consumer_secret = 'h4ICsG26QP7UEngdnK2KlaluQM3r89bJ2fZ0XzcmDMJDfKBAi4'
access_token = '821038831017361408-NwFq0OhyXoB6KCU1hTCQgzLWVGYQdpz'
access_token_secret = 'rVpqUp7PDjez1pplruggwI8MMXlpfisXnWtluA1ed2DlB'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # Interacting with twitter's API
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)  # creating the API object

# Refrences:-https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

# Extracting Tweets
results = []
keyword = 'Canada OR University OR Dalhousie University OR Canada Education OR Halifax'
for tweet in tweepy.Cursor(api.search, q=keyword, lang="en", tweet_mode='extended', truncated=False).items(3000):
    results.append(tweet)


# function to remove punctuation
def remove_punct(text):
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text


# cleaning text in tweets
for tweet in results:
    text = tweet._json
    if 'retweeted_status' in text:
        text = tweet.retweeted_status.full_text
        clean_text = p.clean(text)
        more_clean = emoji_pattern.sub(r'', clean_text)
        ext = re.sub(r'^https?:\/\/.*[\r\n]*', '', more_clean)
        rem_pun = "RT " + remove_punct(ext)
        tweet.retweeted_status.full_text = rem_pun.encode('ascii', 'ignore')
    else:
        text = tweet.full_text
        clean_text = p.clean(text)
        more_clean = emoji_pattern.sub(r'', clean_text)
        ext = re.sub(r'^https?:\/\/.*[\r\n]*', '', more_clean)
        rem_pun = remove_punct(ext)
        tweet.full_text = rem_pun.encode('ascii', 'ignore')


def tweets_df(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]
    test = []
    for tweet in results:
        text = tweet._json
        if 'retweeted_status' in text:
            text1 = tweet.retweeted_status.full_text.decode('utf-8').lower()
            test.append(text1)
        else:
            text1 = tweet.full_text.decode('utf-8').lower()
            test.append(text1)
    data_set["text"] = test
    return data_set


data_set = tweets_df(results)
data = data_set["text"]
data_set.to_csv("tweet3000.csv")
data_set.to_json("tweet3000.json")
list = []

for index,row in data_set.iterrows():
    dict = {
        "Tweet": row["text"].lower()
    }
    list.append(dict)


with open('tweetonly3000.json','w') as f1:
    json.dump(list,f1)
# records = csv.DictReader(data_set["text"])
# collection.insert(records)
