# compounding interest table
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# df_interest_rate_month = pd.DataFrame({"Month":["01-2025","02-2025","03-2025"],
                                       # "InterestRate":[10,11,12]})
# ==============================================================================
# read the dataset
# df_interest_rate_month = pd.read_csv(r"E:\Sharukkhan\AllProjects\Reshma_interest_tracker\InterestTrackerApp\interest_rate_table.csv")

# Convert column to datetime and reformat
# df_interest_rate_month['Month'] = pd.to_datetime(df_interest_rate_month['End of'], format='%b-%y').dt.strftime('%m-%Y')
# df_interest_rate_month['InterestRate'] = df_interest_rate_month["Interest Rate"]*100
#==============================================================================



#---------REQUIRED FUNCTIONS----------
## --------- CREATE A LIST OF DATES------------
def list_of_dates(start_date,end_date):
    from datetime import datetime, timedelta
    
    # Define start and end dates
    # start_date = "15-02-2024"
    # end_date = "31-03-2024"
    
    # Convert strings to datetime objects
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    
    # Generate the list of dates
    date_list = []
    current = start
    while current <= end:
        date_list.append(current.strftime("%d-%m-%Y"))  # Format as string (optional)
        current += timedelta(days=1)
    
    # Print the list
    return date_list
#------------------------------------------------

# take month and date from date string 
from datetime import datetime 
def format_month_year(date_str):
    """
    Converts a date string in 'dd-mm-yyyy' format to 'Mon-YYYY' format (e.g., 'Jan-2025').

    Args:
        date_str (str): The date string (e.g., "01-01-2025")

    Returns:
        str: Formatted month and year (e.g., "Jan-2025")
    """
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%m-%Y")

# Example usage
formatted = format_month_year("01-01-2025")
print(formatted)  # Output: Jan-2025

#-------------------------------------------------
# to know start of the month
def start_of_the_month(date_str):
    from datetime import datetime
    
    #date_str = "01-01-2025"
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    
    # Check if it's the first day of the month
    if date_obj.day == 1:
        return "Month_Start"
    else:
        return ""

start_of_the_month("01-01-2025")

#-------------------------------------------------
# to know start of the month
def end_of_the_month(date_str):
    from datetime import datetime, timedelta

    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    
    # Add one day and check if month changes
    next_day = date_obj + timedelta(days=1)
    if next_day.month != date_obj.month:
        return "Month_End"
    else:
        return ""

end_of_the_month("31-01-2025")

#-------------------------------------------------
# compound_interest
def compound_interest(principal, rate, time, frequency):
    """
    Calculate compound interest.

    Parameters:
    principal (float): The initial amount of money (P)
    rate (float): The annual interest rate in percent (r)
    time (float): Time in years (t)
    frequency (int): Number of times interest is compounded per year (n)

    Returns:
    float: The total amount after interest (A)
    """
    time = time/360
    amount = principal * (1 + rate / (frequency * 100)) ** (frequency * time)
    interest = amount - principal
    return round(interest, 10)

# Example: ₹10,000 at 10% interest, compounded monthly for 2 years
total = compound_interest(1000, 10, 1, 12)
print(f"Total amount after 2 years: ₹{total}")

#-------------------------------------------------
def simple_interest(principal, annual_rate_percent, round_to, days_in_year=360):
    """
    Calculate daily interest for a given principal and annual interest rate.
    
    Args:
        principal (float): The principal amount.
        annual_rate_percent (float): The annual interest rate in percentage (e.g., 10 for 10%).
        days_in_year (int): The number of days in a year (default is 360).
        round_to (int): Number of decimal places to round the result (default is 6).
        
    Returns:
        float: The daily interest amount rounded to the specified decimal places.
    """
    annual_rate = annual_rate_percent / 100
    daily_interest = (annual_rate / days_in_year) * principal
    return round(daily_interest, round_to)

# Example usage
# print(simple_interest(1000, 10))  # Output: 0.277778


# CREATING FUNCTION
def interest_cal_function(val_principal, start_date, end_date, lst_payment_date, lst_payment_amount,df_interest_rate_month, val_decimal_point):
    
    # try:
    #     # Convert column to datetime and reformat
    #     df_interest_rate_month['Month'] = pd.to_datetime(df_interest_rate_month['End of'], format='%b-%y').dt.strftime('%m-%Y')
    #     df_interest_rate_month['InterestRate'] = df_interest_rate_month["Interest Rate"]*100
    # except:
    #     pass
    lst_rate_used = []
    lst_month_start = []
    lst_month_end_compounding = []
    lst_principal = []
    lst_interest_accured = []
    lst_interest_accured_cumulation = []
    lst_compounded = []
    lst_total_amount = []
    lst_payment_done = []
    
    # lst_dates = list_of_dates("01-01-2025","15-03-2025")
    lst_dates = list_of_dates(start_date,end_date)
    
    for date in lst_dates:
        
        # adding rate
        val1_date = format_month_year(date)
        val2_interest = round(df_interest_rate_month[df_interest_rate_month["Month"] == val1_date]["InterestRate"].values[0],10)
        lst_rate_used.append(val2_interest)
        
        # adding month start
        lst_month_start.append(start_of_the_month(date))
        
        # Adding month end(compounding)
        lst_month_end_compounding.append(end_of_the_month(date))
        
        # interest Accured
        val_interest_accured = simple_interest(val_principal, val2_interest, val_decimal_point)
        lst_interest_accured.append(val_interest_accured)
        
        # payment done
        print(lst_payment_date)
        print(lst_payment_amount)
        for payment_date, payment_amt in zip(lst_payment_date,lst_payment_amount):
            if date == payment_date:
                lst_payment_done.append(payment_amt)
            else:
                lst_payment_done.append(0)
        if lst_payment_date == []:
            lst_payment_done.append(0)
                
    df_final = pd.DataFrame({
        "Date":lst_dates,
        "Rate_Used":lst_rate_used,
        "Payment_Done":lst_payment_done,
        "Month_Start":lst_month_start,
        "Compounding":lst_month_end_compounding,
        "Interest_Accured_SI":lst_interest_accured
        })
        
    # -----------interest rate cumulation value-------------
    lst_interest_accured_cumulation = []
    val_mul = 1
    for i in range(len(df_final)):
        if df_final["Month_Start"][i] == "Month_Start" or i == 0:
            val_mul = 1
            val = df_final["Interest_Accured_SI"][i] * val_mul
            lst_interest_accured_cumulation.append(val)
        else:
            val_mul = val_mul + 1
            val = df_final["Interest_Accured_SI"][i] * val_mul
            lst_interest_accured_cumulation.append(val)
    df_final["Interest_Accured_SI_Cumulation"] = lst_interest_accured_cumulation
    #------------------------------------------------
    # total amount
    lst_total_amount = []
    
    for i in range(len(df_final)):
        if df_final["Compounding"][i] == "Month_End":
            val = df_final["Interest_Accured_SI_Cumulation"][i] + val_principal
            lst_total_amount.append(val)
        else:
            lst_total_amount.append(val_principal)
    df_final["Total_amount"] = lst_total_amount
    
    
    
    # FILL THE REST OF VALUES
    for i in range(len(df_final)):
        if i == 0:
            continue
        else:
            if df_final["Payment_Done"][i] != 0:
            # elif df_final["Payment_Done"][i] != 0:
                # substitute the values
                df_final["Interest_Accured_SI"][i] = df_final["Interest_Accured_SI"][i-1]
                df_final["Interest_Accured_SI_Cumulation"][i] = df_final["Interest_Accured_SI_Cumulation"][i-1] + df_final["Interest_Accured_SI"][i]
                df_final["Total_amount"][i] = df_final["Total_amount"][i-1]
                
                # calculation
                val_TAA = df_final["Interest_Accured_SI_Cumulation"][i]+df_final["Total_amount"][i]
                val_payment_amt = df_final["Payment_Done"][i]
                val = val_TAA - val_payment_amt
                val_SI = simple_interest(val, df_final["Rate_Used"][i+1],val_decimal_point)
                
                df_final["Interest_Accured_SI"][i+1] = val_SI
                
                df_final["Interest_Accured_SI_Cumulation"][i+1] = df_final["Interest_Accured_SI"][i+1]
                df_final["Total_amount"][i+1] = val
                
                print(df_final.iloc[i+1,:])
            elif df_final["Payment_Done"][i-1] != 0:
                continue
                
            elif df_final["Compounding"][i] == "Month_End":
                #substitute the previous values
                df_final["Interest_Accured_SI"][i] = df_final["Interest_Accured_SI"][i-1]
                df_final["Interest_Accured_SI_Cumulation"][i] = df_final["Interest_Accured_SI_Cumulation"][i-1] + df_final["Interest_Accured_SI"][i]
                df_final["Total_amount"][i] = df_final["Total_amount"][i-1]
                
                df_final["Total_amount"][i] = df_final["Total_amount"][i-1] + df_final["Interest_Accured_SI_Cumulation"][i]
                
                
            elif df_final["Month_Start"][i] == "Month_Start" and df_final["Compounding"][i-1] == "Month_End":
               
                val_SI = simple_interest(df_final["Total_amount"][i-1], df_final["Rate_Used"][i],val_decimal_point)
                df_final["Interest_Accured_SI"][i] = val_SI
                
                df_final["Interest_Accured_SI_Cumulation"][i] = df_final["Interest_Accured_SI"][i]
                df_final["Total_amount"][i] = df_final["Total_amount"][i-1]

            

            else:
                if df_final["Payment_Done"][i-1] != 0:
                    df_final["Interest_Accured_SI"][i+1] = df_final["Interest_Accured_SI"][i-1]
                    df_final["Interest_Accured_SI_Cumulation"][i] = df_final["Interest_Accured_SI_Cumulation"][i-1] + df_final["Interest_Accured_SI"][i]
                    # df_final["Total_amount"][i] = df_final["Total_amount"][i-1]
                    # pass
                else:   
                    df_final["Interest_Accured_SI"][i] = df_final["Interest_Accured_SI"][i-1]
                    df_final["Interest_Accured_SI_Cumulation"][i] = df_final["Interest_Accured_SI_Cumulation"][i-1] + df_final["Interest_Accured_SI"][i]
                    df_final["Total_amount"][i] = df_final["Total_amount"][i-1]
    
    #--------------------------------------------            
    # payment done        
    lst_payment_cumu = []
    for i in range(len(df_final)):
        if df_final["Compounding"][i] == "Month_End":
            lst_payment_cumu.append(df_final["Total_amount"][i])
        else:
            val = df_final["Interest_Accured_SI_Cumulation"][i] + df_final["Total_amount"][i]
            lst_payment_cumu.append(val)
    
    df_final["Total_amount_Accured"] = lst_payment_cumu 
    # answer table is
    #--------------------------------------------
    # Adding Start and End date
    lst_start_end_date = []
    for i in range(len(df_final)):
        if df_final["Date"][i] == start_date:
            lst_start_end_date.append("Start_Date")
        elif df_final["Date"][i] == end_date:
            lst_start_end_date.append("End_Date")
        else:
            lst_start_end_date.append("")
    df_final["Start_End_Date"] = lst_start_end_date
    #--------------------------------------------
    # Adding Payment Date
    lst_payment_column = []
    for i in range(len(df_final)):
        if df_final["Payment_Done"][i] != 0:
            lst_payment_column.append("Payment_Day")
            try:
                lst_payment_column[-2] = "Payment_Day-1"
            except:
                continue
            try:
                lst_payment_column.append("Payment_Day+1")
                
            except:
                continue
        else:
            lst_payment_column.append("")
    if lst_payment_date == []:
        df_final["Payment_Days"] = lst_payment_column     
    else:
        df_final["Payment_Days"] = lst_payment_column[:-1]
    
    # rearrange columns
    column_reorder = ['Date', 'Rate_Used', 'Payment_Done', 'Month_Start', 'Compounding',
                     'Start_End_Date', 'Payment_Days', 'Interest_Accured_SI', 'Interest_Accured_SI_Cumulation',
                     'Total_amount', 'Total_amount_Accured']
    df_final = df_final[column_reorder]
    
    # monthly_table
    lst_monthly_index = []
    for i in range(len(df_final)):
        if df_final["Month_Start"][i] == "Month_Start":
            lst_monthly_index.append(i)
        elif df_final["Compounding"][i] == "Month_End":
            lst_monthly_index.append(i)
        elif df_final["Start_End_Date"][i] != "":
            lst_monthly_index.append(i)
        elif df_final["Payment_Days"][i] != "":
            lst_monthly_index.append(i)
        else:
            continue
        
        
    # take only monthly table
    df_final_monthly = df_final.iloc[lst_monthly_index,:]
    return df_final, df_final_monthly

# df_final.to_csv(r"E:\Sharukkhan\AllProjects\Reshma_interest_tracker\file_to_check.csv")

#------------------------------------------------

# val_principal = 1000
# start_date = "01-01-2025"
# end_date = "15-03-2025"
# # lst_dates = list_of_dates("01-01-2025","15-03-2025")
# # payment done
# # lst_payment_date = ["15-02-2025"]
# # lst_payment_amount = [1000]
# lst_payment_date = []
# lst_payment_amount = []

# df_interest_rate_month = pd.read_csv(r"E:\Sharukkhan\AllProjects\Reshma_interest_tracker\InterestTrackerApp\interest_rate_table.csv")
# df_interest_rate_month['Month'] = pd.to_datetime(df_interest_rate_month['End of'], format='%b-%y').dt.strftime('%m-%Y')
# df_interest_rate_month['InterestRate'] = df_interest_rate_month["Interest Rate"]*100

# x = interest_cal_function(val_principal, start_date, end_date, lst_payment_date, lst_payment_amount, df_interest_rate_month)

