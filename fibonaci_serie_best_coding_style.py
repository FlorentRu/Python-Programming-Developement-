'''
Created on Jul 21, 2018

'''
def fib(x):
    a,b=0,1
    while a<=x: 
        print(a,' ')
        a,b=b,a+b
fib(15)
