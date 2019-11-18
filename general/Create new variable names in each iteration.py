# give new variable name for each iteration
count = 0
for i in range(1,11):
    stri = "value"+str(i)
    exec(stri+"="+str(count))
    count = count + 1
    
    


















