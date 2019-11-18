# creating a dataframe
df = pd.DataFrame({'data':[5,2,3,4,5,6,7,8,9,10,500],
                   'data1':[1,2,3,4,5,6,7,800,9,10,5]})
# 500 is outlier
# 800 IS OUTLIER
from scipy import stats

# the values after 3rd standard deviation is eliminate in this process
# by using z-score
# set your standard deviation value here

a=3
df=df[(np.abs(stats.zscore(df)) < a).all(axis=1)]
#  .all(axis=1) ensures that for each row, all column satisfy the constraint. 

# for z-score
df1=pd.DataFrame({'data':[1,2,3,4,5,6,7,800,9,10,500]})
from scipy import stats
df1=stats.zscore(df1)


# thank you

# added test create new branch
