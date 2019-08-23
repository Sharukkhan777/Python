
# A Python program to print all  
# combinations of given length 
from itertools import combinations 
import numpy as np

# create a list of numbers
import random
list_rand = random.sample(range(1,100), 3)

# Dataframe
df = list_rand

# r is gaps
# i.e.,)sample size
r = 2
# n = Number of rows
n=len(df)
l=np.arange(n).tolist()

comb = combinations(l, r) 
# Print the obtained combinations 
l1=[]
for i in list(comb): 
    l1.append(i)
    
  
    








