'''
Created on Feb 20, 2019

'''
def reverse_number(num):
    sum=0
    while num!=0:
        t=num%10
        sum=(sum*10)+t
        num=num//10
    return sum
print("welcome to number palindrom application")
num=int(input("enter a value to check whether its a palindrome or not"))
x=reverse_number(num)
print("the reverse of given number %d is %d"%(num,x))
if x==num:
    print("the given number is a palindrome")
else:
    print("its not a palindrom number")
