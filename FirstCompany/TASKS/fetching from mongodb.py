# cohorts

# importing libraries
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

collection = db.transaction
data_transaction = pd.DataFrame(list(collection.find({}, 
    { 
        "_id" : "$_id", 
        "amount" : "$amount",
        "gateway":"$gateway",
        "transaction_date":"$transaction_date",
        "user_id":"$user_id"
    })))
# article view log

collection2 = db.article_views_log
data_article_views_log = pd.DataFrame(list(collection2.find()))

data_article_views_log.to_csv(r'C:\Users\prasannaraj.s\Desktop\sharukkhan\mongoDB\articleviewlog.csv', header=True)





