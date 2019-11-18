"""A simple example of how to access the Google Analytics API."""

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import csv
import sys
import numpy as np
import argparse
import sys
import csv
import string
import mysql.connector as sql
def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service
  
def get_results(service, profile_id):
    a = []
    for pag_index in range(0, 20):
     
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the past seven days.
        a.append(service.data().ga().get(
                ids='ga:109774184',
                start_date='2019-08-20',
                end_date='2019-08-20',
                dimensions = 'ga:dimension2,ga:ScreenName,ga:sourceMedium',
                metrics='ga:screenviews',
                filters='ga:dimension2!~0',
                start_index=str(pag_index*10000+1),
                max_results=str(pag_index*10000+10000)).execute())
    return a
        
def print_results(results):
  header = [h['name'][3:] for h in results[0].get('columnHeaders')]
  df_temp=pd.DataFrame()
  for i in results:
    df = pd.DataFrame(i.get('rows'), columns = header)
    try:
      if not df_temp.empty:
        df_temp = pd.concat([df,df_temp])
      else:
        df_temp = df
    except AttributeError:
        pass
          
  #df.dropna(inplace = True)
  #df1 = df["dimension5"].str.split("-", n = 2, expand = True)
  #df2 = pd.DataFrame(df1)
  print(df_temp)
  #df_temp = df_temp.drop_duplicates()
  df_temp.to_csv(r'H:\prasannaraj.s\sharukkhan\python codes\Target bucket fill\AppUserPageViews.csv')
  
    
def main():
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'API Project-12b174df7b20.json'
        

    # Authenticate and construct service.
    service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=[scope],
            key_file_location=key_file_location)

    profile_id = '12884381'#get_first_profile_id(service)
    print_results(get_results(service, profile_id))
main()

# play sound
import winsound
duration = 100  # milliseconds
freq = 4440  # Hz
winsound.Beep(freq, duration)
winsound.Beep(freq, duration)
winsound.Beep(freq, duration)
#winsound.PlaySound("C:/Users/prasannaraj.s/Downloads/audio (1).wav",winsound.SND_ASYNC)


