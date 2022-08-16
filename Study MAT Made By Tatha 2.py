# -*- LISTs in python -*-
"""
Created on Sat Jul 30 19:49:56 2022

@author: Tathagata Sau
"""

# Lists
friends=["Usmi", "USMI","USMI","USMI","usmi",'Ayusmita','tatha'] #anything like strings numbers booleans
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])# not includes the last number in range
friends[1]="USmiiiiii"
print(friends)
#list fuction
lucky_numbers=[27,7,19,45,55]
friends.extend(lucky_numbers)
print(friends)
friends.extend(friends)
print(friends)
lucky_numbers.extend(friends)
print(lucky_numbers)
friends.append("sayantan")
print(friends)
friends.insert(1,"Pratyasha")
print(friends)
friends.remove("sayantan")
print(friends)
friends.pop(4)
print(friends)
#friends.clear()
print(friends)
print(friends.index("Pratyasha"))
print(friends.count("USMI"))

friends2=["Usmi", "Tathagata","Sudipta","Rishik","Siddhartha",'Ayusmita','Pratyasha']
friends2.sort()
print(friends2)
friends2.reverse()
print(friends2)
copy_friends= friends2.copy()
print(friends2)