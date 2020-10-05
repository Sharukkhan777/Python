# 2. Statistical test
# Z- test for a population mean(variance known and equal)

import scipy.stats as st
import statistics as stat
inp = input("Press 1 for parameter values known\nPress 2 for data(series) known\n")

if inp == "1":
    n1 = float(input("n1 = "))
    n2 = float(input("n2 = "))
    x_bar1 = float(input("x_bar1 = "))
    x_bar2 = float(input("x_bar2 = "))
    sigma = float(input("sigma = "))
    on_tw = input("Press 1 for one tail\nPress 2 for two tail\n")
    los = float(input("level_of_sig = "))
    z_cal = (x_bar1 - x_bar2)/(sigma*(( (1/n1)+(1/n2) )**0.5))
    # calculate the z_table value
    if on_tw == 1:
        cl = st.norm.ppf(1 - los)
        if z_cal < cl:
            print("Null Hypothesis accepted:")
            print("No Significant difference between assumed pop mean and sample mean")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between assumed pop mean and sample mean")
        
    else:
        lower_cl = st.norm.ppf(0+(los/2))
        upper_cl = st.norm.ppf(1-(los/2))
        if (z_cal > lower_cl) and (z_cal < upper_cl):
            print("Null Hypothesis accepted:")
            print("No Significant difference between assumed pop mean and sample mean")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between assumed pop mean and sample mean")
    
else:
    data1 = eval(input("Input your data1 in list format, [1,2,3]\n"))
    data2 = eval(input("Input your data2 in list format, [1,2,3]\n"))
    n1 = len(data1)
    n2 = len(data2)
    x_bar1 = stat.mean(data1)
    x_bar2 = stat.mean(data2)
    sigma = float(input("sigma = "))
    on_tw = input("Press 1 for one tail\nPress 2 for two tail\n")
    los = float(input("level_of_sig = "))
    z_cal = (x_bar1 - x_bar2)/(sigma*(( (1/n1)+(1/n2) )**0.5))
    # calculate the z_table value
    if on_tw == 1: 
        cl = st.norm.ppf(1 - los)
        if z_cal < cl:
            print("Null Hypothesis accepted:")
            print("No Significant difference between means of two population")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between means of two population")
        
    else:
        lower_cl = st.norm.ppf(0+(los/2))
        upper_cl = st.norm.ppf(1-(los/2))
        if (z_cal > lower_cl) and (z_cal < upper_cl):
            print("Null Hypothesis accepted:")
            print("No Significant difference between means of two population")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between means of two population")
    
    
