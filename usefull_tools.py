# -*- the module -*-
"""
Created on Sat Aug  6 13:00:21 2022

@author: Tathagata Sau
"""

import random
feet_in_mile = 5200
meters_in_kilometer=1000
beatles=["Usmi","Ayusmita","So", "I","Wanted", "tell", "you Something","for a long time"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1,num)