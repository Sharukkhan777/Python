import pandas as pd
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
import pandas as pd
import json


df=pd.read_excel(r"C:\Users\prasannaraj.s\Desktop\sharukkhan\mongoDB\Transaction.xlsx",sheet_name='card')

import matplotlib as m
m.pyplot.boxplot(df['amount'])



