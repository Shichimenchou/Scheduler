import datetime
from pathlib import Path

def block():
    now = datetime.datetime.now()
    mins = now.minute + 60 * now.hour
    # print("The current block is " + str(mins // 30))
    return mins // 30

blk = block()
day = (datetime.datetime.today().weekday() + 1) % 7
schedule = []

if day == 0:
    F = open(str(Path.home()) + "/Schedule/" + "sunday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 1: 
    F = open(str(Path.home()) + "/Schedule/" + "monday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 2:
    F = open(str(Path.home()) + "/Schedule/" + "tuesday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 3:
    F = open(str(Path.home()) + "/Schedule/" + "wednesday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 4:
    F = open(str(Path.home()) + "/Schedule/" + "thursday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 5:
    F = open(str(Path.home()) + "/Schedule/" + "friday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 6:
    F = open(str(Path.home()) + "/Schedule/" + "saturday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]

print(schedule[blk])
