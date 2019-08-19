import pandas as pd

# read excel file
df = pd.read_excel(r'C:\Users\SHARUK KHAN_2\Downloads\for python.xlsx')




users = list(df['user_id'])
hour = list(df['less than an hour'])


n = len(users)
users_n = []
hour_n = []
for i in range(n-1):
    if (hour[i]==0):
        continue
    elif(hour[i]!=0)&(hour[i+1]==0):
        users_n.append(users[i])
        hour_n.append(hour[i])
    else:
        continue

# creating the data base
dataframe = pd.DataFrame({'user_id':users_n,
                         'less than one hour':hour_n})

dataframe.to_csv(r'C:\Users\SHARUK KHAN_2\Desktop\revisedforpython.csv')







