# OBJECT ORIENTED PROGRAM SIMPLE EXAMPLE
'''
https://www.youtube.com/watch?v=ic6wdPxcHc0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=54
'''
class Computer:
    def __init__(self,cpu,ram):
        self.cpuu = cpu
        self.ramm = ram
        
        
        
    def config(self):
        print('Config is ',self.cpuu,self.ramm)
        
        
# creating object        
com1 = Computer("i5",16)
com2 = Computer('Ryzen 3',8)       
        
# function calling
com1.config()
com2.config()       
         
     







  




 