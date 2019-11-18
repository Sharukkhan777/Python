# create a datafrme
import pandas as pd

df1 =pd.DataFrame({'user_id':['A','A']
                ,'pageviews':[1,2]})


df2 = pd.DataFrame({'user_id':['A','A','A','B','C']
                    ,'date':[1,2,3,1,2]})


merge = pd.merge(df1,df2,on = 'user_id',how = 'left')



















