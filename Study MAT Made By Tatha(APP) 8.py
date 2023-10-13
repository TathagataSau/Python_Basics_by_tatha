# -*- object(taken from the class) -*-
"""
Created on Sun Aug  7 20:25:01 2022

@author: Tathagata Sau
"""
from Student import Student

student1 = Student("Mahesh", "Computer science", 9.5, True)
student2 = Student("MAhesh Dalle", "ECE", 9.73, False)

print(student1.name)
print(student2.name)
print(student2.gpa)# here the gpa will give the major value as it is being changed in the mail class

#the values is being passed in the __init__ 
#inheritance .... pretty easy no need to bothr writing another code
