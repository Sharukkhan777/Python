import mysql.connector as sql
from pandas.io.json import json_normalize
from datetime import date
from datetime import time
from datetime import datetime
from datetime import datetime, date
import numpy as np
from datetime import datetime, timedelta
import datetime
import pandas as pd
import pymysql.cursors
import pymysql
import csv
db_connection = sql.connect(host='mysqltest.vigital.local', database='user_vikatan', user='root', password='83X41Pqd3sfy')
df = pd.read_sql("SELECT `User_Id`, `Order_Type`, `Amount`, `Payment_Date`  FROM `payment` WHERE `Trans_Status` = 0 AND `Status` = 1",db_connection)
df['Date'] = df['Payment_Date'].dt.date
pd.to_datetime(df['Date'])
start_date_all = pd.Timestamp('today')
df['Amount'] = df['Amount'].astype('int64')
end_date_all = start_date_all - datetime.timedelta(days=365)
data_transaction2 = (df['Payment_Date'] < start_date_all) & (df['Payment_Date'] > end_date_all)
df1 = df.loc[data_transaction2]
df2 = df1[['User_Id', 'Order_Type', 'Amount','Payment_Date', 'Date']]
df3 = df2[(df2.Order_Type == 'Single_Issue_Product') | (df2.Order_Type == 'Online_Subscription') | (df2.Order_Type == 'FLP')]
db_connectionPayment = sql.connect(host='mysql.vikatan.in', database='ga', user='datauser', password='bNUHyQVC7u4HvDxL')
sqlDelete = ("Delete from Payment")
sql = ("INSERT INTO Payment (User_Id, Order_Type, Amount, Payment_Date, Date) VALUES (%s, %s, %s, %s, %s)")
mycursor = db_connectionPayment.cursor()
mycursor.execute(sqlDelete)
mycursor.executemany(sql, df3.values.tolist())
db_connectionPayment.commit()
