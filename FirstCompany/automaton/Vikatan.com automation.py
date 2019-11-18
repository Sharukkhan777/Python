# input phase
#------------------------------------------------------------------------------
dd = 25
mm = 8  # dont put '08' put '8' only
yyyy = 2019
#------------------------------------------------------------------------------

"""A simple example of how to access the Google Analytics API."""

from googleapiclient.discovery import build
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
from pandas.io.json import json_normalize
from datetime import date
from datetime import time
from datetime import datetime
from datetime import datetime, date
from datetime import datetime, timedelta
import datetime
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
#````````````Organic_Search`````````````````````````````````````````````````````
def get_results_Organic_Search(service, profile_id):
    a = []
    date1 = datetime.date(yyyy, mm, dd)
    date2 = datetime.date(yyyy, mm, dd)
    day = datetime.timedelta(days=1)
    while date1 <= date2:
        for pag_index in range(0,100):
            a.append(service.data().ga().get(
                ids='ga:12884381',
                start_date=date1.strftime('%Y-%m-%d'),
                end_date=date1.strftime('%Y-%m-%d'),
                dimensions = 'ga:channelGrouping',
                metrics='ga:pageviews,ga:users',
                filters='ga:channelGrouping==Organic Search',
                start_index=str(pag_index*10000+1),
                max_results=str(pag_index*10000+10000)).execute())
        date1 += day
    return a     
    
            
            
def print_results_Organic_Search(results):
    #shows header
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

  return df_temp

  
#``````````````````````````````````````````````````````````````````````````````
#````````````Direct`````````````````````````````````````````````````````
def get_results_Direct(service, profile_id):
    a = []
    date1 = datetime.date(yyyy, mm, dd)
    date2 = datetime.date(yyyy, mm, dd)
    day = datetime.timedelta(days=1)
    while date1 <= date2:
        for pag_index in range(0,100):
            a.append(service.data().ga().get(
                ids='ga:12884381',
                start_date=date1.strftime('%Y-%m-%d'),
                end_date=date1.strftime('%Y-%m-%d'),
                dimensions = 'ga:channelGrouping',
                metrics='ga:pageviews,ga:users',
                filters='ga:channelGrouping==Direct',
                start_index=str(pag_index*10000+1),
                max_results=str(pag_index*10000+10000)).execute())
        date1 += day
    return a     
    
            
            
def print_results_Direct(results):
    #shows header
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

  return df_temp

#``````````````````````````````````````````````````````````````````````````````
#````````````Referral`````````````````````````````````````````````````````
def get_results_Referral(service, profile_id):
    a = []
    date1 = datetime.date(yyyy, mm, dd)
    date2 = datetime.date(yyyy, mm, dd)
    day = datetime.timedelta(days=1)
    while date1 <= date2:
        for pag_index in range(0,100):
            a.append(service.data().ga().get(
                ids='ga:12884381',
                start_date=date1.strftime('%Y-%m-%d'),
                end_date=date1.strftime('%Y-%m-%d'),
                dimensions = 'ga:channelGrouping',
                metrics='ga:pageviews,ga:users',
                filters='ga:channelGrouping==Referral',
                start_index=str(pag_index*10000+1),
                max_results=str(pag_index*10000+10000)).execute())
        date1 += day
    return a     
    
            
            
def print_results_Referral(results):
    #shows header
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

  return df_temp

#``````````````````````````````````````````````````````````````````````````````
#````````````Display`````````````````````````````````````````````````````
def get_results_Display(service, profile_id):
    a = []
    date1 = datetime.date(yyyy, mm, dd)
    date2 = datetime.date(yyyy, mm, dd)
    day = datetime.timedelta(days=1)
    while date1 <= date2:
        for pag_index in range(0,100):
            a.append(service.data().ga().get(
                ids='ga:12884381',
                start_date=date1.strftime('%Y-%m-%d'),
                end_date=date1.strftime('%Y-%m-%d'),
                dimensions = 'ga:channelGrouping',
                metrics='ga:pageviews,ga:users',
                filters='ga:channelGrouping==Display',
                start_index=str(pag_index*10000+1),
                max_results=str(pag_index*10000+10000)).execute())
        date1 += day
    return a     
    
            
            
def print_results_Display(results):
    #shows header
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

  return df_temp

#``````````````````````````````````````````````````````````````````````````````
#````````````Email`````````````````````````````````````````````````````
def get_results_Email(service, profile_id):
    a = []
    date1 = datetime.date(yyyy, mm, dd)
    date2 = datetime.date(yyyy, mm, dd)
    day = datetime.timedelta(days=1)
    while date1 <= date2:
        for pag_index in range(0,100):
            a.append(service.data().ga().get(
                ids='ga:12884381',
                start_date=date1.strftime('%Y-%m-%d'),
                end_date=date1.strftime('%Y-%m-%d'),
                dimensions = 'ga:channelGrouping',
                metrics='ga:pageviews,ga:users',
                filters='ga:channelGrouping==Email',
                start_index=str(pag_index*10000+1),
                max_results=str(pag_index*10000+10000)).execute())
        date1 += day
    return a     
    
            
            
def print_results_Email(results):
    #shows header
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

  return df_temp

#``````````````````````````````````````````````````````````````````````````````
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
    
    organic_search = print_results_Organic_Search(get_results_Organic_Search(service, profile_id))
    direct = print_results_Direct(get_results_Direct(service, profile_id))
    referral = print_results_Referral(get_results_Referral(service, profile_id))
    display = print_results_Display(get_results_Display(service, profile_id))
    email = print_results_Email(get_results_Email(service, profile_id))
    
    
    df_new = pd.concat([organic_search,direct,referral,display,email])
    df_new.to_csv(r'H:\prasannaraj.s\sharukkhan\temp\UserPageViews.csv')
main()
    
    
    