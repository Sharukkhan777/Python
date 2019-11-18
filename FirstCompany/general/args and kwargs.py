'''
Introduction to *args and **kwargs
'''
#``````````````````````````````````````````````````````````````````````````````
# *args(arguments)
def person(name,*data):
    print(name)
    print(data)
    
person('navin',28,'Mumbai',461643645)
    
# OUTPUT >>>
# navin
# (28, 'Mumbai', 461643645) # return as tuple

#``````````````````````````````````````````````````````````````````````````````
# **kwargs(keyword arguments)
def person(name,**data):
    print(name)
    print(data['age'])
    
person('navin',age = 28,city = 'Mumbai',ph_no = 461643645)
    
# OUTPUT >>>
# navin
# {'age': 28, 'city': 'Mumbai', 'ph_no': 461643645} # return as dictionary

#``````````````````````````````````````````````````````````````````````````````

# kwargs(keyword arguments) with accessing element
def person(name,**data):
    print(name)
    print(data['age']) # access age from data
    
person('navin',age = 28,city = 'Mumbai',ph_no = 461643645)
    
# OUTPUT >>>
# navin
# 28        

#``````````````````````````````````````````````````````````````````````````````


import re

str = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", str)
x


































