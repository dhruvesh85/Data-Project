#Second file to execute
#It will clean all dimension files created before by removing duplicate and inserting index.
import pandas as pd

df = pd.read_csv("orderdim.csv")
df.drop_duplicates(subset=None, inplace=True)
df['orderid'] = df.index
df.to_csv("orderdimcl.csv", index=False)

df = pd.read_csv("orderlinedim.csv")
df.drop_duplicates(subset=None, inplace=True)
df['orderlineid'] = df.index
df.to_csv("orderlinedimcl.csv", index=False)

df = pd.read_csv("productdim.csv")
df.drop_duplicates(subset=None, inplace=True)
df['productid'] = df.index
df.to_csv("productdimcl.csv", index=False)

df = pd.read_csv("addressdim.csv")
df.drop_duplicates(subset=None, inplace=True)
df['addressid'] = df.index
df.to_csv("addressdimcl.csv", index=False)

df = pd.read_csv("clientdim.csv")
df.drop_duplicates(subset=None, inplace=True)
df['clientid'] = df.index
df.to_csv("clientdimcl.csv", index=False)

df = pd.read_csv("timedim.csv")
df.drop_duplicates(subset=None, inplace=True)
df['timeid'] = df.index
df.to_csv("timedimcl.csv", index=False)






