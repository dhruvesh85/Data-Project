#first file to execute
#It will create all dimension file
import pandas as pd
df = pd.read_csv("sales_data_sample.csv")
df[['month', 'DATE_ID', 'year']] = df.ORDERDATE.str.split("/", expand=True)
df.to_csv("sales_data_sample1.csv", index=False)
df.to_csv("orderdim.csv", columns=['ORDERNUMBER', 'STATUS'], index=False)
df.to_csv("orderlinedim.csv", columns=['ORDERLINENUMBER', 'PRICEEACH', 'QUANTITYORDERED'], index=False)
df.to_csv("productdim.csv", columns=['PRODUCTLINE', 'MSRP', 'PRODUCTCODE'], index=False)
df.to_csv("addressdim.csv",columns=['ADDRESSLINE1', 'ADDRESSLINE2', 'CITY', 'STATE', 'POSTALCODE', 'COUNTRY', 'TERRITORY'], index=False)
df.to_csv("clientdim.csv", columns=['CUSTOMERNAME', 'PHONE', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME'], index=False)
df1 = pd.read_csv("sales_data_sample1.csv")
df1.to_csv("timedim.csv", columns=['DATE_ID', 'QTR_ID', 'MONTH_ID', 'YEAR_ID'], index=False)
