#forth file to execute
#It will create fact table.
import pandas as pd

df = pd.read_csv("aftercleaning.csv")
# df.to_csv("orderdimfin.csv", columns=['orderid','ORDERNUMBER', 'STATUS'], index=False)
# df.to_csv("orderlinedimfin.csv", columns=['orderlineid','ORDERLINENUMBER', 'PRICEEACH', 'QUANTITYORDERED'], index=False)
# df.to_csv("productdimfin.csv", columns=['productid','PRODUCTLINE', 'MSRP', 'PRODUCTCODE'], index=False)
# df.to_csv("addressdimfin.csv",columns=['addressid','ADDRESSLINE1', 'ADDRESSLINE2', 'CITY', 'STATE', 'POSTALCODE', 'COUNTRY', 'TERRITORY'], index=False)
# df.to_csv("clientdimfin.csv", columns=['clientid','CUSTOMERNAME', 'PHONE', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME'], index=False)
# df.to_csv("timedimfin.csv", columns=['timeid','DATE_ID','QTR_ID', 'MONTH_ID', 'YEAR_ID'], index=False)
df.to_csv("fact.csv", columns=['timeid','clientid','addressid', 'productid', 'orderid','orderlineid','SALES','DEALSIZE'])