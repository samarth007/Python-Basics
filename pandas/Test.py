import pandas as pd
import numpy as np
import requests

res= requests.get('https://api.github.com/repos/pandas-dev/pandas/issues')
print(res)

js= res.json() #coverting response into list
print(type(js))
df=pd.DataFrame(js) #converting list into dataframe
csv_data= df.to_csv('test.csv')  #converting dataframe into csv and creating a file
 