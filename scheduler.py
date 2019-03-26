import datetime
from pathlib import Path

def block():
    now = datetime.datetime.now()
    mins = now.minute + 60 * now.hour
    # print("The current block is " + str(mins // 30))
    return mins // 30

def blockToTime(blk):
    hour = blk // 2
    half = blk % 2
    if half == 0:
        return str(hour)
    else:
        return str(hour) + ":30"

blk = block()
day = (datetime.datetime.today().weekday() + 1) % 7
schedule = []

if day == 0:
    F = open(str(Path.home()) + "/Projects/Schedule/" + "sunday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 1: 
    F = open(str(Path.home()) + "/Projects/Schedule/" + "monday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 2:
    F = open(str(Path.home()) + "/Projects/Schedule/" + "tuesday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 3:
    F = open(str(Path.home()) + "/Projects/Schedule/" + "wednesday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 4:
    F = open(str(Path.home()) + "/Projects/Schedule/" + "thursday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 5:
    F = open(str(Path.home()) + "/Projects/Schedule/" + "friday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]
if day == 6:
    F = open(str(Path.home()) + "/Projects/Schedule/" + "saturday.txt", "r")
    schedule += F.readlines()
    for i in range(0, 48):
        schedule[i] = schedule[i][:-1]

if blk == 47:
    print(blockToTime(blk) + " - " + schedule[blk] + " : 0 - " + schedule[0])
else:
    print(blockToTime(blk) + " - " + schedule[blk] + " : " + blockToTime(blk + 1) + " - " + schedule[blk + 1])
