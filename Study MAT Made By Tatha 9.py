# -*- MCQ QUESTION OBJECT -*-
"""
Created on Sun Aug  7 20:46:42 2022

@author: Tathagata Sau
"""
from question import question
question_prompts =[
    "What are you Usmi?\n(a) Sweet \n(b) Cute \n(c) Sweet and cute Both?  \n(d)only one of them\n\nans:",
    "What am I Usmi?\n(a) Sweet \n(b) Cute \n(c) Sweet and cute Both?  \n(d)none of them\n\nans:",
    "what is your most Favourite thing?\n (a) Jhumkas \n(b)Coding \n(c)Ice Cream \n(d)Tathagata\n\nans:"
    
]
questions = [
    question(question_prompts[0],"c"),
    question(question_prompts[1],"d"),
    question(question_prompts[2],"b"),
]

def run_test(questions):
    score=0
    for question in questions:   #question object in question array
        answer = input(question.prompt)
        if answer ==question.answer:
            score +=1
    print("you got"+ str(score)+"/" +str(len(questions))+"correct")    
run_test(questions)    








