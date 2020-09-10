#Third file to execute
#It will add indexes of dimension tables to sales data

import pandas as pd
df = pd.read_csv("sales_data_sample1.csv")

df1 = pd.read_csv("orderdimcl.csv")
for index, row in df1.iterrows():
    c = row["orderid"]
    df.loc[(df["ORDERNUMBER"] == row['ORDERNUMBER']) & (df["STATUS"] == row["STATUS"]), "orderid"] = c

df1 = pd.read_csv("orderlinedimcl.csv")
for index, row in df1.iterrows():
    c = row["orderlineid"]
    df.loc[(df["QUANTITYORDERED"] == row['QUANTITYORDERED']) & (df["PRICEEACH"] == row["PRICEEACH"]) & (df["ORDERLINENUMBER"] == row["ORDERLINENUMBER"]), "orderlineid"] = c

df1 = pd.read_csv("productdimcl.csv")
for index, row in df1.iterrows():
    c = row["productid"]
    df.loc[(df["PRODUCTLINE"] == row['PRODUCTLINE']) & (df["MSRP"] == row["MSRP"]) & (df["PRODUCTCODE"] == row["PRODUCTCODE"]), "productid"] = c

df1 = pd.read_csv("addressdimcl.csv")
for index, row in df1.iterrows():
    c = row["addressid"]
    df.loc[(df["ADDRESSLINE1"] == row['ADDRESSLINE1']) & (df["ADDRESSLINE2"] == row["ADDRESSLINE2"]) & (df["CITY"] == row["CITY"]) & (df["STATE"] == row["STATE"]) & (df["POSTALCODE"] == row["POSTALCODE"]) & (df["COUNTRY"] == row["COUNTRY"])& (df["TERRITORY"] == row["TERRITORY"]), "addressid"] = c

df1 = pd.read_csv("clientdimcl.csv")
for index, row in df1.iterrows():
    c = row["clientid"]
    df.loc[(df["CUSTOMERNAME"] == row['CUSTOMERNAME']) & (df["CONTACTLASTNAME"] == row["CONTACTLASTNAME"]) & (df["CONTACTFIRSTNAME"] == row["CONTACTFIRSTNAME"]) & (df["PHONE"] == row["PHONE"]), "clientid"] = c

df1 = pd.read_csv("timedimcl.csv")
for index, row in df1.iterrows():
    c = row["timeid"]
    df.loc[(df["DATE_ID"] == row['DATE_ID']) & (df["QTR_ID"] == row["QTR_ID"]) & (df["MONTH_ID"] == row["MONTH_ID"]) & (df["YEAR_ID"] == row["YEAR_ID"]), "timeid"] = c

df.to_csv("aftercleaning.csv", index=False)
