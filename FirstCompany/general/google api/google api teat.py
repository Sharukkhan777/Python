# google api
'''
Website : https://www.youtube.com/watch?v=cnPlKLEGR7E


'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 4 scopes because spares are there
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# creds
creds = ServiceAccountCredentials.from_json_keyfile_name('googleapi.json',scope)

# clients
client = gspread.authorize(creds)

# accessing the sheets
sheet = client.open('test').sheet1

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

insertRow = ["hello", 5, "red", "blue"]
sheet.add_rows(row,4)  # Insert the list as a row at index 4

sheet.update_cell(2,2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet


































