# -*- Dictionaries + guessing game+Loops-*-
"""
Created on Fri Aug  5 01:26:36 2022

@author: Tathagata Sau
"""
#"key":"value"
monthConversions ={
    "Jan":"January",
    "Feb":"February",
    3:"March",
    "apr":"April",
    }
print(monthConversions['apr'])
print(monthConversions.get("Heart","Mahesh")) #default value
print(monthConversions[3])
#### While LOOP
i=1
while i<=10:
    print(i)
    i+=1
print("Done with the Loop alredy??")
#guessing game

secret_word="love"
guess=""
guess_count=0
guess_limit =3
out_of_guesses= False
#guess=input(print("Enter guess:"))

while guess !=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("Enter guess :")
        guess_count+=1
    else:
        out_of_guesses=True
if out_of_guesses:
    print("out of guess,You Lose!")
else:
    print("you win!")

    
