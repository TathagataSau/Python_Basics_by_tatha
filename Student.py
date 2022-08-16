# -*- Classes -*-
"""
Created on Sun Aug  7 20:16:05 2022

@author: Tathagata Sau
"""
#creating own datatypes
class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):    #2 underscores are there  
        self.name = name #actual object.name will be the name of the class
        self.major = gpa
        self.gpa = major # just makin twigs for the better understanding
        self.is_on_probation = is_on_probation
        
           