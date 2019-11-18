from pymongo import MongoClient
import pymongo
import pandas as pd
import json
from pandas.io.json import json_normalize
from datetime import date
from datetime import time
from datetime import datetime
from datetime import datetime, date
import numpy as np
from datetime import datetime, timedelta
import datetime

uri = "mongodb://admin:e828z4GP6A9D@10.10.2.66:30128/appappo?authSource=admin"
client = MongoClient(uri)
db = client.appappo 

# transaction 
collection1 = db.transaction
data_transaction = pd.DataFrame(list(collection1.find()))
data_transaction.to_csv(r'C:\Users\prasannaraj.s\Desktop\sharukkhan\mongoDB\Transaction.csv', header=True)
#data_transaction = data_transaction['gateway']=='wallet'
#data_transaction['wallet']=np.where(data_transaction['gateway']=='wallet')

data_transaction2 = data_transaction['gateway']=='wallet'
df2 = data_transaction.loc[data_transaction2]

Paid = data_transaction.set_index('gateway').filter(like='card', axis=0)

PaidUnique2 = Paid.drop_duplicates(['user_id'], keep='last')
PaidUnique2 = PaidUnique2.rename(columns={'transaction_date': 'recent_transaction'})

PaidUnique3 =PaidUnique2 [['user_id','recent_transaction']]

merge_df = pd.merge(df2,PaidUnique3,how='left', on ='user_id')
merge_df.to_csv(r'C:\Users\prasannaraj.s\Desktop\sharukkhan\merge_df.csv', header=True)

merge_df['recent_transaction'].drop


#data_transaction = data_transaction.gateway.filter(like='wallet', axis=0)
# read excel
onboard=pd.read_excel(r'C:\Users\prasannaraj.s\Desktop\sharukkhan\tasks\appappo_profile (7).xlsx')
Paid = onboard.set_index('User Type').filter(like='paid', axis=0)
Paid['paid_user'] = np.ones(982,dtype = str)     
paidUserID = onboard[['User_id','User Type']]
paidUserID['User_id'].astype(object)

# overall 20%
overall20=pd.read_excel(r'C:\Users\prasannaraj.s\Desktop\sharukkhan\tasks\all category20%.xlsx',sheet_name='all 20%')

paidUserID = paidUserID.rename(columns={'User_id': 'user_id'})
data_trans = data_transaction['user_id'].astype(object)
#merge
merge20 = pd.merge(data_trans, paidUserID, on='user_id', how='left')

Paid_trans = merge20.set_index('User Type').filter(like='paid' , axis=0)








































