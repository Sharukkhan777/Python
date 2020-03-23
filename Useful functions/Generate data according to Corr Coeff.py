# generate the data for the given correlation coefficient

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# enter your correlation coefficient
R = float(input("Enter your needed correlation coefficient = "))
num = int(input("Enter your number of rows = "))

# generate the data
r = None
while r != R:
    x = random.sample(range(1, 100), num)
    y = random.sample(range(1, 100), num)
    r = np.corrcoef(x, y)
    r = r[0,1]

# Just see How the data looks like
plt.scatter(x,y)

# create a DataFrame
data = pd.DataFrame({'X':x,
                     'Y':y})

