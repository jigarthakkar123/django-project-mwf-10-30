'''
class : It is a group of different type of variables & function.
Collection of objects.

Object : It is an instance of class.
'''
class Student:

    def getData(self,fname,lname):
        self.f=fname
        self.l=lname
    def putData(self):
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1=Student()
f=input("Enter First Name : ")
l=input("Enter Last Name : ")

s1.getData(f,l)
s1.putData()
