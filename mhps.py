# Written by Luke Darling

import sys, random

def simulate():
    doors = [True, False, False]

    for i in range(random.randrange(10)):
        random.shuffle(doors)
    
    selected = random.randrange(3)

    for i in range(len(doors)):
        if selected == i:
            continue

        if doors[i] == True:
            continue

        doors.pop(i)
        if selected > i:
            selected -= 1
        break

    if selected == 1:
        selected = 0
    else:
        selected = 1
    
    if doors[selected] == True:
        return 1
    else:
        return 0

def run(runs):
    runs = int(runs)
    ran = 0
    correct = 0

    for _ in range(runs):
        ran += 1
        correct += simulate()

    print(correct / ran)

if len(sys.argv) > 1:
    run(sys.argv[1])
else:
    print("Usage: python " + sys.argv[0] + " <simulations>")