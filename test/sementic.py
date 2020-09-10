import pandas as pd
import math
from csv import DictReader
# df = pd.read_csv("newsfinal1.csv")
# df['combined'] = df.title + ' ' + df.description + ' ' + df.content
# # df['index'] = df.index
# df.to_csv("newsfinal1combined.csv",columns=['combined'],index=False)

# df = pd.read_csv("newsfinal1combined.csv")
# df['index'] = df.index
# df.to_csv("newsfinal1combined.csv",columns=['index','combined'],index=False)


df = pd.read_csv("newsfinal1combined.csv")
final_count =[]
canada=[]
canada_count=0
uni=[]
uni_count =0
dal_uni=[]
dal_uni_count =0
hali=[]
hali_count=0
business=[]
business_count=0
with open("newsfinal1combined.csv", 'r') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        file_name = "{}.txt".format(row["index"])
        if row["combined"]:  # if this field is not empty
            line = row["combined"] + '\n'
        else:
            continue
        with open(file_name, 'w') as output:
            output.write(line)

with open("newsfinal1combined.csv", 'r') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        canada1 = "false"
        uni1 = "false"
        dal_uni1 = "false"
        hali1 = "false"
        business1 = "false"
        file1 = row["combined"]
        index1 = int(row["index"])
        # print(file1)
        # print(index1)
        if 'canada' in file1:
            canada1="true"
            canada_count = canada_count + 1
        if 'university' in file1:
            uni1="true"
            uni_count = uni_count+ 1
        if 'dalhousie university' in file1:
            dal_uni1="true"
            dal_uni_count = dal_uni_count + 1
        if 'halifax' in file1:
            hali1="true"
            hali_count = hali_count + 1
        if 'business' in file1:
            business1="true"
            business_count = business_count +1


        canada.append(canada1)
        hali.append(hali1)
        uni.append(uni1)
        dal_uni.append(dal_uni1)
        business.append(business1)



    final_count.append(canada_count)
    final_count.append(uni_count)
    final_count.append(hali_count)
    final_count.append(dal_uni_count)
    final_count.append(business_count)


df['canada']=canada
df['university']=uni
df['dalhousie university']=dal_uni
df['halifax']=hali
df['business']=business
df.to_csv("newsupdatedcombined.csv",index=False)

df = pd.DataFrame(columns=['Search Query', 'df'])
df['Search Query']=['canada','university','halifax','dalhousie university','business']
df['df']=final_count
df.to_csv("calculated1.csv",index=False)

total_doc=len(canada)
total =[]
div=[]
logg=[]
df = pd.read_csv("calculated1.csv")
for index, row in df.iterrows():
    cf=row["df"]
    division=format(total_doc/cf, '.2f')
    logaritm=format(math.log(float(division),10), '.2f')
    div.append(division)
    logg.append(logaritm)
    total.append(total_doc)

df['N']=total
df['N/df']=div
df['log10(N/df)']=logg
df.to_csv("calculated1.csv",index=False)


articles=[]
df = pd.read_csv("newsupdatedcombined.csv")
for index, row in df.iterrows():

    if(row['canada']):
        articles.append(row["combined"])


df = pd.DataFrame(columns=['article'])
df['article']=articles
df.to_csv("onlycanada_articles.csv",index=False)

df =pd.read_csv("onlycanada_articles.csv")
can=[]
fm=[]
total_words=[]
max=0
maxfm=0.0
for index, row in df.iterrows():
    counts = dict()
    words = row["article"].split()

    for word in words:
        if word in counts:
            counts[word] += 1
            if(word == "canada"):
                canadacon=counts[word]
        else:
            counts[word] = 1
    fmcon = format(canadacon/len(words), '.2f')
    fm.append(fmcon)
    can.append(canadacon)
    total_words.append(len(words))
    if(max<canadacon):
        max=canadacon
    if(maxfm<float(fmcon)):
        maxfm= float(format(canadacon/len(words), '.2f'))
df['frequency of word canada(f)']=can
df['total words(m)']=total_words
df['f/m']=fm
df.to_csv("onlycanada_articles.csv")

df =pd.read_csv("onlycanada_articles.csv")
df1=pd.DataFrame(columns=['max','article'])
max_fm=[]
article=[]

for index, row in df.iterrows():
    if(row['frequency of word canada(f)'] == max):
        print(max)
        print("Article having highest frequency of word canada:"+row['article'])
        max_fm.append(max)
        article.append(row['article'])
df1['max']=max_fm
df1['article']=article
df1.to_csv("ans2.csv",index=False)

df1=pd.DataFrame(columns=['max f/m','article'])
df =pd.read_csv("onlycanada_articles.csv")
max_fm=[]
article=[]
for index, row in df.iterrows():
    if(row['f/m'] == maxfm):
        print(maxfm)
        print("Article having highest f/m of word canada:"+row['article'])
        max_fm.append(maxfm)
        article.append(row['article'])
df1['max f/m']=max_fm
df1['article']=article
df1.to_csv("ans3.csv",index=False)
