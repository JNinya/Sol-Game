import console
import random
import time

def randomLine():
    frequency = 0.1
    line = ""
    for i in range(50):
        if (random.random() < frequency):
            line += "|"
        else:
            line += " "
    return line
        

while True:
    print(randomLine())
    time.sleep(0.008)



"""

lines = ["riots", "riiiiiiiots", "do you remember", "DO YOU REMEMBER"]

class Riot:
    def __init__(self, lengthOfIs, lengthOfOs):
        self.lengthOfIs = lengthOfIs
        self.lengthOfOs = lengthOfOs

"""
#DO YOU REMEMBER
#RIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOT




