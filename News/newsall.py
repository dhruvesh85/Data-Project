import json
import pandas
import requests
import re
import string
import pymongo

# The headers remain the same for all the requests
headers = {'Authorization': ''}
# client = pymongo.MongoClient("")
# db = client.assigndb
# collection=db['news']

# Refrences:-https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf
# All the endpoints in this section
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

def remove_punct(text):
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text
keyword=['canada','University','Dalhousie University','Canada Education','Halifax','Moncton','Toronto']

everything_news_url = 'https://newsapi.org/v2/everything'
results = []
for key in keyword:
    everything_payload = {'q': key, 'language': 'en', 'pageSize': '100'}
    response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)
    response_json_string = json.dumps(response.json())
    response_dict = json.loads(response_json_string)
    articles_list = response_dict['articles']
    for art in articles_list:
        if(art['content'] != None):
            abc = art['content']
            clean = emoji_pattern.sub(r'', abc)
            abcd = remove_punct(clean)
            abcd = abcd.replace("\r", "")
            abcd = abcd.replace("\n", "")
            art['content'] = (abcd.encode('ascii', 'ignore')).decode("utf-8").lower()

        if(art['description'] != None):
            abc = art['description']
            clean = emoji_pattern.sub(r'', abc)
            abcd = remove_punct(clean)
            abcd = abcd.replace("\r", "")
            abcd = abcd.replace("\n", "")
            art['description'] = (abcd.encode('ascii', 'ignore')).decode("utf-8").lower()

        if (art['title'] != None):
            abc = art['title']
            clean = emoji_pattern.sub(r'', abc)
            abcd = remove_punct(clean)
            abcd = abcd.replace("\r", "")
            abcd = abcd.replace("\n", "")
            art['title'] = (abcd.encode('ascii', 'ignore')).decode("utf-8").lower()
        results.append(art)
print(results)
df = pandas.read_json(json.dumps(results))
df.to_csv("newsfinal1.csv",index=False)
# data = df["content"]
# list = []

# for index,row in df.iterrows():
#     dict = {
#         "Tweet": row["content"].lower()
#     }
#     list.append(dict)

# with open('newsfinal1.json','w') as f1:
#     json.dump(list,f1)
# collection.insert_many(list)


# data.to_json("newsfinal1.json")
