import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import csv
import sys
import argparse
import string
import mysql.connector as sql
from pandas.io.json import json_normalize
from datetime import datetime, timedelta
from datetime import datetime, date
from datetime import date
from datetime import time
from datetime import datetime
import datetime

db_connection1 = sql.connect(host='mysqltest.vigital.local', database='user_vikatan', user='root', password='83X41Pqd3sfy')
db1 = pd.read_sql("SELECT * FROM `user_subscription_updated` WHERE `End_Date` >= '2019-09-10 00:00:00' AND `Status` = 1 ORDER BY `user_subscription_updated`.`End_Date` DESC",db_connection1)
db1=db1.drop_duplicates(['User_Id'], keep='first')

db_connection = sql.connect(host='mysqltest.vigital.local', database='admin_vikatan', user='root', password='83X41Pqd3sfy')
db = pd.read_sql("SELECT Module_Id,Subscription_Period,Unique_Name,Subscription_Id FROM `master_subscription`",db_connection)

###########    Merge 1  #############

df1 = pd.merge(db1, db, on='Subscription_Id', how='left')

######## Paymenet table

db_connection2 = sql.connect(host='mysqltest.vigital.local', database='user_vikatan', user='root', password='83X41Pqd3sfy')
payment = pd.read_sql("SELECT Order_Id,Amount,Payment_Date FROM `payment` WHERE `Status` = 1 ORDER BY `Payment_Date` DESC",db_connection2)

######     Merge 2

df2 = pd.merge(df1, payment, on='Order_Id', how='left')
df2.to_csv(r'C:\Users\magesh.c\Vikatan projects\Weekly current users reports\Req data.csv')
df2.rename(columns={'User_Id_x':'User_Id'},inplace=True)

########### Master user to find Email and Mobile

db_connection3 = sql.connect(host='mysqltest.vigital.local', database='user_vikatan', user='root', password='83X41Pqd3sfy')
phne = pd.read_sql("SELECT User_Id,Email_Id,Mobile_Number FROM `master_user`",db_connection3)

########## Merge 3

Required_Data = pd.merge(df2,phne, on='User_Id', how='left')

### filter doesnt contain @vikatan and 1

new_df = Required_Data[~Required_Data['Email_Id'].str.contains('@vikatan', na=False)]
new_df=new_df [new_df .Amount != 1]

### filter doesnt contain 0

zero_Payment=new_df [new_df .Amount == 0]
new_df=new_df [new_df .Amount != 0]

### count of users without 0 and 1 and vikatan
Count_users=new_df.User_Id.count()

### count of users without 0 and 1 and vikatan
Count_zero_users=zero_Payment.User_Id.count()

#### Req data and zero payment data alone
new_df.to_csv(r'C:\Users\magesh.c\Vikatan projects\Req_data(1).csv')
zero_Payment.to_csv(r'C:\Users\magesh.c\Vikatan projects\Weekly current users reports\Final report\zero_Payment.csv')

#### All subscriptions of zero payment users

db_connection4 = sql.connect(host='mysqltest.vigital.local', database='user_vikatan', user='root', password='83X41Pqd3sfy')
All_Subs= pd.read_sql("SELECT * FROM `user_subscription_updated` WHERE `Status` = 1 ORDER BY `user_subscription_updated`.`End_Date` DESC",db_connection4)

Zero_payment_Users=zero_Payment['User_Id']
Zero_All_Subs= pd.merge(Zero_payment_Users, All_Subs, on='User_Id', how='left')

Final_data= pd.merge(Zero_All_Subs, payment, on='Order_Id', how='left')
Final_data.to_csv(r'C:\Users\magesh.c\Vikatan projects\Weekly current users reports\Final report\Final_data.csv')

### Remove duplicates User_Id and Order_Id

Final_data=Final_data.drop_duplicates(['User_Id','Order_Id'], keep='first')

#### Pivot

Final_users=Final_data.pivot_table(values='Amount',aggfunc='sum',index='User_Id')
Final_users=Final_users [Final_users .Amount != 0]
Count_Paid_zero_users=Final_users.Amount.count()

Final_users.to_csv(r'C:\Users\magesh.c\Vikatan projects\Weekly current users reports\Final report\Final_data_2.csv')

######

Overall_paidusers=int(Count_users)+int(Count_Paid_zero_users)

#### Print the output
print('Count of users is',Count_users)
print('Count of zero payment users is',Count_zero_users)
print('Count of Actual_zero payment users is',Count_Paid_zero_users)
print('Count of overall users is',Overall_paidusers)




































