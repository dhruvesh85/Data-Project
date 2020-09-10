# import pandas as pd
# df = pd.read_csv("clecle.csv")
# print(df['text'])
# str=df['text'].to_string()
# str_list =str.lower().split()
# list=['canada','university','dalhousie']
# unique_words = set(str_list)
# for words in unique_words:
#     if words in list:
#      print('Frequency of ', words, 'is :', str_list.count(words))
#     # else:
#       #print('Frequency of ', words, 'is :', str_list.count(words))

import pandas as pd
import pymongo
import json
import string
client = pymongo.MongoClient("mongodb://dhruvesh:root@3.21.156.171/assigndb")
db = client.assigndb
collection = db['test2']
with open('tweetfinal.json') as f:
  data = json.load(f)
df = pd.DataFrame(data)
with open('newsfinal.json') as f1:
  data1 = json.load(f1)
df1 = pd.DataFrame(data1)
print(df)
list = []
for index,row in df.iterrows():
    dict = {
        "Tweet": row["Tweet"]
    }
    list.append(dict)
for index,row in df1.iterrows():
    dict = {
        "Tweet": row["Tweet"]
    }
    list.append(dict)
collection.insert_many(list)