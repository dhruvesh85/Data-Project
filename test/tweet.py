import tweepy # To consume Twitter's API
import pandas as pd
import preprocessor as p
import re
import string

####input your credentials here
consumer_key = 'Ap3f7BSkmIyqI84ePYCXtluq4'
consumer_secret = 'h4ICsG26QP7UEngdnK2KlaluQM3r89bJ2fZ0XzcmDMJDfKBAi4'
access_token = '821038831017361408-NwFq0OhyXoB6KCU1hTCQgzLWVGYQdpz'
access_token_secret = 'rVpqUp7PDjez1pplruggwI8MMXlpfisXnWtluA1ed2DlB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Interacting with twitter's API
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API (auth) #creating the API object

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

# Extracting Tweets
results = []
keyword='Canada OR University OR Dalhousie University OR Canada Education OR Halifax'
for tweet in tweepy.Cursor(api.search, q=keyword, lang="en", tweet_mode='extended', truncated=False).items(30):
    results.append(tweet)

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

for tweet in results:
    text = tweet.full_text
    clean_text = p.clean(text)
    more_clean=emoji_pattern.sub(r'', clean_text)
    rem_pun = remove_punct(more_clean)
    ext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", rem_pun)
    tweet.full_text = ext

def tweets_df(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])
    data_set["text"] = [tweet.full_text for tweet in results]
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]
    data_set["Hashtags"] = [tweet.entities.get('hashtags') for tweet in results]
    return data_set

data_set = tweets_df(results)
data_set.to_json(r' file3000.json')