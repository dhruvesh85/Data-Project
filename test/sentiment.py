import pandas as pd
import json
import os
import csv

df = pd.read_csv("tweet3000.csv")
positive = []
negative = []
polarity = []
pos_visual =dict()
neg_visual =dict()
positive_store =[]
negative_store = []
list = []
with open('positive.txt', 'r') as f:
    for a in f:
        positive.append(a.strip())
print(positive)
with open('negative.txt', 'r') as f:
    for a in f:
        negative.append(a.strip())
for index, row in df.iterrows():
    counts = dict()
    positive_tweet = dict()
    negative_tweet = dict()
    words = row["text"].split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    list.append(counts)
    with open('my_file', 'a') as f:
        json.dump(counts, f)
        f.write(os.linesep)

    for count, value in counts.items():
        # print(count)
        positive_sum = 0
        negative_sum = 0

        for pos in positive:
            if (count == pos):
                positive_tweet[count] = value
                if count in pos_visual:
                    pos_visual[count] += value
                else:
                    pos_visual[count] = value
                # print(positive_tweet)
        for neg in negative:
            if (count == neg):
                negative_tweet[count] = value
                if count in neg_visual:
                    neg_visual[count] += value
                else:
                    neg_visual[count] = value
                # print("negative:", negative_tweet)

        for pos, val in positive_tweet.items():
            positive_sum = positive_sum + val

        for neg, val in negative_tweet.items():
            negative_sum = negative_sum + val

    # print("possum:", positive_sum)
    # print("negsum:", negative_sum)
    if (bool(negative_tweet)):
        negative_store.append(negative_tweet)
    else:
        negative_store.append("null")

    if (bool(positive_tweet)):
        positive_store.append(positive_tweet)
    else:
        positive_store.append("null")

    if (positive_sum > negative_sum):
        polarity.append("positive")
    elif(negative_sum > positive_sum):
        polarity.append("negative")
    else:
         polarity.append("neutral")

# print(polarity)
# print(positive_store)
# print(negative_store)
print(pos_visual)
print(neg_visual)
df['polarity']=polarity
df['positive_bag']=positive_store
df['negative_bag']=negative_store
df.to_csv("visual.csv",columns=['text','polarity','positive_bag','negative_bag'],index=False)

with open("final_visual.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["word","frequency","type"])
    for i in pos_visual:
      writer.writerow([i, pos_visual[i],"positive"])

    for i in neg_visual:
      writer.writerow([i, neg_visual[i],"negative"])

f.close()


# for pos in positive:
#     if(count is pos):
#         print(count)
#         print(value)
#
# for neg in negative:
#      if(count is neg):
#          print(count)
#          print(value)


# # print(list)
# with open('my_file', 'r') as f:
#     list1=f.read()
#
# print(list1)
