n1 = float(input("n1 = "))
n2 = float(input("n2 = "))
t1 = float(input("t1 = "))
t2 = float(input("t2 = "))
on_tw = input("Press 1 for one tail\nPress 2 for two tail\n")
los = float(input("level_of_sig = "))

R1 = n1/t1
R2 = n2/t2
# Z calculated value
Z_cal = (R1 - R2)/( ((R1/t1) + (R2/t2))**(0.5))

# Z tabulated value
import scipy.stats as st
st.norm.ppf(.975)
if on_tw == 1:
    cl = st.norm.ppf(1 - los)
    if Z_cal < cl:
        print("Null Hypothesis accepted:")
        print("No difference between counts")
    else:
        print("Null Hypothesis Rejected:")
        print("Difference between counts")
        
else:
    lower_cl = st.norm.ppf(0+(los/2))
    upper_cl = st.norm.ppf(1-(los/2))
    if (Z_cal > lower_cl) and (Z_cal < upper_cl):
        print("Null Hypothesis accepted:")
        print("No difference between counts")
    else:
        print("Null Hypothesis Rejected:")
        print("Difference between counts")
        

