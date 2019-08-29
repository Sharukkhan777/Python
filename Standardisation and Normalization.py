# Standardisation And Normalization

# data
l=[3,3,4,4,6]
#------------------------------------------------------------------------------
# standardisation

# mean
n = len(l)
summ = 0
for i in range(n):
    summ = summ + l[i]
mean = summ/n
# sample standard deviation(n-1)
sd = 0
for i in range(n):
    sd = sd + (l[i] - mean)**2
sd = (sd/(n-1))**(1/2)
# calculating z score
z = []
for i in range(n):
    z_score = (l[i]-mean)/sd
    z.append(z_score)

z # type "z" to see your z scores
#------------------------------------------------------------------------------
# normalization
mini = min(l)
maxi = max(l)

normali = [] 
for i in range(n):
    normal = (l[i]-mini)/(maxi - mini)
    normali.append(normal)

normali # type"normali" to see normalize data
    
#normalization values lies between 0 to 1





