import json
import pandas
import requests
import re
import string
# The headers remain the same for all the requests
headers = {'Authorization': '53cf3c1b925d4731b1fc921bfa905d3a'}

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
keyword=['canada','University','Dalhousie University','Canada Education','Halifax']
# To fetch the top headlines
#top_headlines_url = 'https://newsapi.org/v2/top-headlines'
# To fetch news articles

everything_news_url = 'https://newsapi.org/v2/everything'
# To retrieve the sources
#sources_url = 'https://newsapi.org/v2/sources'

# Add parameters to request URL based on what type of headlines news you want
#keyword='Canada OR University OR Dalhousie University OR Halifax OR Canada Education OR Moncton OR Toronto'
# All the payloads in this section
#headlines_payload = {'category': 'business', 'country': 'us'}
everything_payload = {'q': keyword, 'language': 'en', 'pageSize': '100'}
#sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}

# Fire a request based on the requirement, just change the url and the params field

# Request to fetch the top headlines
# response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)

# Request to fetch every news article
response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)

# Request to fetch the sources
# response = requests.get(url=sources_url, headers=headers, params=sources_payload)


# To store the relevant json data to a csv

# Convert response to a pure json string
response_json_string = json.dumps(response.json())

# A json object is equivalent to a dictionary in Python
# retrieve json objects to a python dict
response_dict = json.loads(response_json_string)

# Info about articles is represented as an array in the json response
# A json array is equivalent to a list in python
# We want info only about articles
articles_list = response_dict['articles']
print(articles_list)

for art in articles_list:
    if(art['content'] != None):
     abc = art['content']
     #print(abc)
     # abcd=remove_punct(abc)
     clean = emoji_pattern.sub(r'', abc)
     abcd = remove_punct(clean)
     abcd = abcd.replace("\r", "")
     abcd = abcd.replace("\n", "")
     art['content'] = (abcd.encode('ascii', 'ignore')).decode("utf-8")
     print(art['content'])




# We want info only about sources
# sources_list = response_dict['sources']
# And then you can specify one of these sources explicitly if you like while fetching the news

# Convert articles list to json string , convert json string to dataframe , write df to csv!
df = pandas.read_json(json.dumps(articles_list))

# Convert sources list to json string , convert json string to dataframe , write df to csv!
#df = pandas.read_json(json.dumps(sources_list))
#print(df)
# Using Pandas write the json data to a csv
df.to_csv("n453645463.csv")
df.to_json("n453645463.json")