'''
Created on Jun 1, 2019

'''
a = 10
b = 20
c = a + b

#Normal string concatenation
print("sum of", a , "and" , b , "is" , c) 

#convert variable into str
print("sum of " + str(a) + " and " + str(b) + " is " + str(c)) 

# if you want to print in tuple way
print("Sum of %s and %s is %s: " %(a,b,c))  # c programming

#New style string formatting
print("sum of {} and {} is {}".format(a,b,c)) 

#in case you want to use repr()
print("sum of " + repr(a) + " and " + repr(b) + " is " + repr(c))
