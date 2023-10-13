# -*- beasic number and String operaions -*-
"""
Created on Sat Jul 30 19:49:56 2022

@author: Tathagata Sau
"""
#from math import*
import math
name = "Rahul"
age = "20"
print("Hi "+ name+" how are you?\""+"I know you are "" old"+" and I love ♥ this thing about you")
print(age.upper().isupper())
print(name.replace("Mahesh","Dalle"))
print(format(-2.0987 - 6.898,".3f"))
num=-7
print(str(num)+" mine and Mahesh's Number")
print(abs(num)) #absolute number
print(pow(num,abs(num)))
print(max(1,2,3,4,46,6,7,66,8))
print(min(1,2,2,3,3,445,3-0,-4,0))
print(round(3.33556))
#now the math functions
#print(floor(3.7))
#print(ceil(7.9))
print(math.floor(3.7))
print(math.ceil(7.9))
print("Square root Using old process of each line using math")
print(math.sqrt(80))
#Input information
Name =input("Type the name Tatha calls you With:")
print("****Now My Favourite Word is \""+ Name +"\" with out a Doubt****")
#calculator
num1=input("give first Input:")
num2=input("give second Input:")
result=float(num1)+float(num2)
print("result is:",result)
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
#game for you STRINGS only
colour=input("input a colour:")
plural_noun=input("enter  a plural noun:")
celebrity=input("name a celebrity:")

print("Roses are "+colour+"\n"+plural_noun+" are Blue\n I love♥"+celebrity)
