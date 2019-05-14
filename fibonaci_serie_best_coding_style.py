'''
Created on Jul 21, 2017

@author: SummitWorks
'''
def fib(x):
    a,b=0,1
    while a<=x: 
        print(a,' ')
        a,b=b,a+b
fib(15)