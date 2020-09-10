import json
import pandas
import omdb
import pymongo
client = pymongo.MongoClient("mongodb://dhruvesh:root@3.21.156.171/assigndb")
db = client.assigndb
collection=db['movies']
api = "cc08a17a"
keyword=['canada','University','Moncton','vancouver','Halifax','Toronto','Alberta','niagara']
presearch=[]
final = []
omdb.set_default('apikey', api) #Refrences:-https://readthedocs.org/projects/omdbpy/downloads/pdf/latest/
for key in keyword:
    presearch=omdb.search(key)
    for pre in presearch:
        abc = omdb.title(pre['title'])
        abc['year']=abc['year'].strip('–')
        final.append(abc)
list = []

df = pandas.read_json(json.dumps(final))
for index,row in df.iterrows():
    dict = {
        "Title": row["title"].lower(),
        "Year": row["year"].lower(),
        "Genre": row["genre"].lower(),
        "ImdbRating": row["imdb_rating"].lower(),
        "Plot": row["plot"].lower()
    }
    list.append(dict)
# collection.insert_many(list)
# print(list)
df.to_csv("movies.csv")
df.to_json("movie.json")




