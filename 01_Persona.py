import pandas as pd
import numpy as np
users=pd.read_csv("/home/efekara/Desktop/bootcamp/2.hafta_EDA/users.csv")
purchases=pd.read_csv("/home/efekara/Desktop/bootcamp/2.hafta_EDA/purchases.csv")
df=purchases.merge(users,on="uid",how="inner")
df.head()
df.shape
agg_df=df.groupby(["country","device","gender","age"]).agg({"price":np.sum}).sort_values(by="price",ascending=False)
agg_df.head()
agg_df.reset_index(inplace=True)
agg_df["age_cat"]=pd.qcut(agg_df["age"], 4, labels=["0_18", "19_25", "26_40", "41_75"])
agg_df.head()
agg_df["customers_level_based"]=[row[0]+"_"+row[1].upper()+"_"+row[2]+"_"+row[5] for row in agg_df.values]
agg_df.head()
agg_df["segment"]=pd.qcut(agg_df["price"], 4, labels=["D","C","B","A"])
agg_df.head()
new_user="TUR_IOS_F_41_75"
new_customers=agg_df[agg_df["customers_level_based"]== new_user]
print(new_customers)



