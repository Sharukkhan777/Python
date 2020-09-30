# 1. Statistical test
# Z- test for a population mean(variance known)

from scipy.stats import t
import statistics as stat
inp = input("Press 1 for parameter values known\nPress 2 for data(series) known\n")

if inp == "1":
    n = float(input("n = "))
    x_bar = float(input("x_bar = "))
    s = float(input("s = "))
    assu_mean = float(input("Assumed pop mean = "))
    on_tw = input("Press 1 for one tail\nPress 2 for two tail\n")
    los = float(input("level_of_sig = "))
    t_cal = (x_bar - assu_mean)/(s/(n**0.5))
    # calculate the t_table value
    if on_tw == 1:
        cl = t.ppf(los,n-1)
        if t_cal < cl:
            print("Null Hypothesis accepted:")
            print("No Significant difference between assumed pop mean and sample mean")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between assumed pop mean and sample mean")
        
    else:
        lower_cl = t.ppf(0+(los/2),n-1) 
        upper_cl = t.ppf(1-(los/2),n-1) 
        if (t_cal > lower_cl) and (t_cal < upper_cl):
            print("Null Hypothesis accepted:")
            print("No Significant difference between assumed pop mean and sample mean")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between assumed pop mean and sample mean")
    
else:
    data = eval(input("Input your data in list format, [1,2,3]\n"))
    n = len(data)
    x_bar = stat.mean(data)
    #------------------------
    # to calculate s
    summ = 0
    for i in range(len(data)):
        summ = summ + (data[i] - x_bar)
    s = (summ/(n-1))**(0.5)
    #------------------------
    assu_mean = float(input("Assumed pop mean = "))
    on_tw = input("Press 1 for one tail\nPress 2 for two tail\n")
    los = float(input("level_of_sig = "))
    z_cal = (x_bar - assu_mean)/(s/(n**0.5))
    # calculate the t_table value
    if on_tw == 1:
        cl = t.ppf(los,n-1)
        if t_cal < cl:
            print("Null Hypothesis accepted:")
            print("No Significant difference between assumed pop mean and sample mean")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between assumed pop mean and sample mean")
        
    else:
        lower_cl = t.ppf(0+(los/2),n-1) 
        upper_cl = t.ppf(1-(los/2),n-1) 
        if (t_cal > lower_cl) and (t_cal < upper_cl):
            print("Null Hypothesis accepted:")
            print("No Significant difference between assumed pop mean and sample mean")
        else:
            print("Null Hypothesis Rejected:")
            print("Significant difference between assumed pop mean and sample mean")
    
    
