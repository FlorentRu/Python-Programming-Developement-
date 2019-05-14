'''
Created on Jul 19, 2017

@author: SummitWorks
'''
import math
def operation_result(op,var1,var2):
    if op==1:
        sum=var1+var2
        print("Addition of %d and %d is %d"%(var1,var2,sum))
    elif op==2:
        sum=var1-var2
        print("Substraction of %d and %d is %d"%(var1,var2,sum))
    elif op==3:
        sum=var1/var2
        print("division of %d and %d is %d"%(var1,var2,sum))
    elif op==4:
        sum=var1*var2
        print("multiplication of %d and %d is %d"%(var1,var2,sum))
    elif op==5:
        sum=var1%var2
        print("modulus of %d and %d is %d"%(var1,var2,sum))
    else:
        print("please enter a valid operator")
    
def operation_geometry(op,var1):
    
    if op==6:
        val=math.sin(var1)
        print("the sin of %d is %f"%(var1,val))
    elif op==7:
        val=math.cos(var1)
        print("the cos of %d is %f"%(var1,val))

    elif op==8:
        val=math.tan(var1)
        print("the tan of %d is %f"%(var1,val))

    else:
        print("please enter a valid oprator")

while True:
    print("-----------1. addition -----------")
    print("-----------2. subtraction -----------")
    print("-----------3. division -----------")
    print("-----------4. multiplication -----------")
    print("-----------5. modulus -----------")
    print("-----------6. sin value -----------")
    print("-----------7. cos value -----------")
    print("-----------8. tan value -----------")
    op=int(input("enter your choice : "))
   
    if (op==1 or op==2 or op==3 or op==4 or op==5):
        var1=int(input("enter first value"))
        var2=int(input("enter second value "))
        operation_result(op,var1,var2);
    elif(op==6 or op==7 or op==8):
        var1=int(input("enter a value"))
        operation_geometry(op,var1)
    else:
        print("Please enter proper value from the menu")
    print("do you want to continue again[ y / n]")
    c=input("enter y to continue n to exit")
    if c=='n' or c== 'N':
        break
    
print("thanks for using this application , visit again")
    
    