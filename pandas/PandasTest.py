import pandas as pd

df=pd.read_csv("./pandas/Pandastest1.csv")
#print(type(df))
#print(type(df.shape))
#row, col=df.shape
#print(row, col)
#print((df[2:5]))
#print(df.columns)
#print(df[['event','day']])
#print(df['temperature'].max())
#print(df['temperature'].min())
#print(df['temperature'].mean())
#print(df[df.temperature>=30]) #df.temperature >=30 return boolean. if result is true then it will print specifc
print(pd.Categorical(df['wind']))
# print(df.dtypes[df.dtypes=='object'])
m=df['temperature'].max()
print(df[df['temperature']==m][['event','day']])
#df.set_index('day',inplace=True) #replaces row values with day
#df.reset_index(inplace=True) #reset to original dataframe
# print(df)
