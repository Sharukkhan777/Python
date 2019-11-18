

# Generators in python


'''
Generators :
    * Definition:
        A generator-function is defined like a normal function, but whenever it needs to generate a value, 
        it does so with the yield keyword rather than return. 
        If the body of a def contains yield, the function automatically becomes a generator function.
        
    * A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
    * We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.
    * Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
 
WEBSITE:
https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/   
    
'''   
 
#``````````````````````````````````````````````````````````````````````````````
# Example code with yield keyword
 
# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 

# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
	i = 1; 

	# An Infinite loop to generate squares 
	while True: 
		yield i*i	#!!!!!!!!!!!!!!!! Warning, if we use return here we get error			 
		i += 1 # Next execution resumes 
				# from this point	 

# Driver code to test above generator 
# function 
for num in nextSquare(): 
	if num > 100: 
		break	
	print(num) 


#``````````````````````````````````````````````````````````````````````````````
# sololearn example

t=(n for n in range(5))
if type(t) == tuple:
    print(len(t))
else:
    print(next(t)) 
#``````````````````````````````````````````````````````````````````````````````
   
    
    
    
    