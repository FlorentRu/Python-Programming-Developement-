'''
Created on Jun 15, 2017

@author: SummitWorks
'''
days = int(input("Enter days: "))
#The divmod(num1, num2) function returns two values , first is the division of num1 and num2 and in second the modulo of num1 and num2.
print("Months = %d Days = %d" % (divmod(days, 30)))