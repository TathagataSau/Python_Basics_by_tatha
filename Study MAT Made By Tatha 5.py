# -*- Loops -*-
"""
Created on Fri Aug  5 02:19:54 2022

@author: Tathagata Sau
"""

##### For Loop

for letter in "Ayusmita Biswas":
    print(letter)
friends = ['Ayusmita','Usmi','Tatha']
for friends in friends:
    print(friends)
    #power operator
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result=result* base_num
    return result
print(raise_to_power(4,7))
#2d list
number_grid=[
    [1,2,3],
    [4,5,6],
    [6,4,3],
    [0]
]
#print(numbe_grid[3][0])
for row in number_grid:
    #print(row)
    for col in row:
        print(col)

"""
Usmi Lang
Vowels -> U
--------
dog -> dug
cat -> cut
"""
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "U"
            else:
                translation = translation + "u"
        else:
            translation= translation + letter
    return translation
print(translate(input("Enter a Phrase:")))

#nvalid input trial and error
try:
    num=int(input("Enter a number:"))
    print(num)
    ''''
except: #each and evry error isn't caught specific err
        print("Invalid Input")
        '''
#so specify the excepts
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input type")
