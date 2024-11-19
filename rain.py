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