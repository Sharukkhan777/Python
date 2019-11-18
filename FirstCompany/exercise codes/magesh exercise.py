# Count of odd and even by users input

l=[]
n= 5
for i in range(n):
    l.append(int(input()))
count_even = 0    
count_odd = 0
for i in l:
    if i%2 == 0:
        count_even = count_even+1
    else:
        count_odd = count_odd+1
#``````````````````````````````````````````````````````````````````````````````
# reverse the string
s=input('Enter your string to reverse :')

n = len(s)
str =''
for i in range(n):
    str = str + s[-1]
    s = s[:-1]
print(str)
#``````````````````````````````````````````````````````````````````````````````
# ascending order

l=[]
n= 5
for i in range(n):
    l.append(int(input()))
asc = [] 
for i in range(n):
    asc.append(min(l))
    l.remove(min(l))
#``````````````````````````````````````````````````````````````````````````````   
# descending order

l=[]
n= 5
for i in range(n):
    l.append(int(input()))
des = [] 
for i in range(n):
    des.append(max(l))
    l.remove(max(l))
#``````````````````````````````````````````````````````````````````````````````
# repeated numbers
list1=[]
n= 5
for i in range(n):
    list1.append(int(input()))

unique_list = [] 

for x in list1: 
    if x not in unique_list: 
        unique_list.append(x)
        
count_list = []
repeated = []
for i in unique_list:
    count = 0
    for j in list1:
        if i == j:
            count = count+1
    count_list.append(count)    
    if count > 1:
        repeated.append(i)
print('Repeated numberes are :',repeated)
#``````````````````````````````````````````````````````````````````````````````
# print random numbers 
a=22/7
fifty = format(a,'.50f')
fifty = str(fifty)
l=[]
for i in fifty:
    if i == ".":
        continue
    else:
        l.append(int(i))

print(l)
#``````````````````````````````````````````````````````````````````````````````
#highest and lowest numbers
# find the min and max not by function
l = [2,2,3,100,4,5,6,7,1]

first = l[0]
n = len(l)
minimum = first
for i in range(1,n):
    other = l[i]
    if minimum < other:
        minimum = minimum
    else:
        minimum = other


# find the min and max not by function
l = [2,2,3,100,4,5,6,7,1]

first = l[0]
n = len(l)
maximum = first
for i in range(1,n):
    other = l[i]
    if maximum < other:
        maximum = other
    else:
        maximum = maximum

# text to column
list_of_names = ['magesh seenu','sharuk khan','a b c']
list_of_new_names = []
for i in list_of_names:
    n = len(i)
    string = ""
    for j in i:
        if j == " ":    # delimited by space
            break
        else:
            string = string + j
    list_of_new_names.append(string)
    
    

















