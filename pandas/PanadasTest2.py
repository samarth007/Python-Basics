import pandas as pd

df=pd.read_csv('./pandas/PandasTest2.csv',skiprows=1) #skiprows, skip 1st row
df1=pd.read_csv('./pandas/PandasTest2.csv',header=None)
df2=pd.read_csv('./pandas/PandasTest2.csv',skiprows=1,header=None
                ,names=['Stocks','PerShare','Rev','PricePer','Ceo'])
df3=pd.read_csv('./pandas/PandasTest2.csv',
                skiprows=1,na_values=['not available','n.a']) #na_values replaces values with NAN
df4=pd.read_csv('./pandas/PandasTest2.csv',skiprows=1,
                na_values={"EPS":['not available'],"Revenue":-1,"Price":"n.a"})



print(df4)