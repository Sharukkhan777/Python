no_of_parti = int(input("No. of participants:"))
no_of_rounds = int(input("No. of rounds:"))
import statistics as st
lst_res = []
for i in range(no_of_parti):
    exec("lst_parti_data_"+str(i+1)+" = []")
    for j in range(no_of_rounds):
        print("___________________________________")
        print("For Round ",j+1," ,For participant ",i+1)
        exec("val = float(input('Enter Oxygen level = '))")
        exec("lst_parti_data_"+str(i+1)+".append(val)")
    exec("res = st.mean(lst_parti_data_"+str(i+1)+")")
    lst_res.append(res)
for i in range(len(lst_res)):
    print("Participant -"+str(i+1)+"- Average Oxygen Level = "+str(lst_res[i]))
