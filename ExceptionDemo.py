#An abnormal situation that arises during the run time of a program is
#called exception.

print("Start Code")
try:
    a=int(input("Enter Value : "))
    b=int(input("Enter Value : "))
    c=a/b
    print("Division : ",c)
    l=[1,2,3,4,5]
    index=int(input("Enter Index Number:"))
    print(l[index])
except Exception as e:
    print("Exception Caught : ",e)

    
print("End Code")
