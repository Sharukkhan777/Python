# test for json to csv demo
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
import csv

db_connection2 = sql.connect(host='mysqltest.vigital.local', database='user_vikatan', user='root', password='83X41Pqd3sfy')
df3 = pd.read_sql("SELECT * FROM `user_payment_details` WHERE `Status` = 1 ORDER BY `Other_Payment_info` DESC",db_connection2)
df3head = df3.head()

import json_to_csv_one_column 

json_to_csv_one_column.json_to_csv_column(df3head['Other_Payment_info'], df3head)


import pandas

json_to_csv_one_column.json_to_csv_column()




















