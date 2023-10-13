# -*- Tuples, Functions, return function -*-
"""
Created on Tue Aug  2 19:28:20 2022

@author: Tathagata Sau
"""

coordinates = (4, 5) #can not change anything from tuples
print(coordinates[0])
#coordinates[0]=10 # doesnot happen co'z its immutable
coordinate=[(4, 5), (5, 6), (7, 8)]
#functions
"""
def hey_you():# crreated a fuction needs to be called
    print('i am u,he is mi')
hey_you() 
"""
def hey_you(name,age):
    print("holA "+name)
    print("age is :",age)
hey_you("Usmi",21)

#function
def cube(num):
    return num*num*num
result= cube(4)    
print(result)
is_male= False
is_tall= False
if is_male and is_tall:
    print("You are not UGLY")
elif is_male and not(is_tall):
    print("Mahesh You'r  Still Dalla ")
else:
    print("Mahesh is Dalle")
#reverse func
num = 1234567
t=str(num)[::-1]
p=int(t)
def max_num(num1,num2,num3):
    if num1>num2 and num1>num3 and "dog"=='dog':
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(max_num(44,7,33))
#input Taking
num1= float(input("Enter the value:"))
op= input("Enter the Operator:")
num2=float(input("Enter the seconf number for calculating:"))
if op =='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("give valid values")

    
