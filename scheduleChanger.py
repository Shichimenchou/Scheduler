import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("day", type=str)
parser.add_argument("time1", type=float)
parser.add_argument("time2", type=float)
parser.add_argument("input", type=str)
args = parser.parse_args()

d = args.day.lower()
b1 = int(args.time1 * 2)
b2 = int(args.time2 * 2)

F = open(str(Path.home()) + "/Schedule/" + d + ".txt", "r")
old = F.readlines()
os.remove(str(Path.home()) + "/Schedule/" + d + ".txt")

f = open(str(Path.home()) + "/Schedule/" + d + ".txt", "w")
if(b1 <= b2):
    for i in range(0, b1):
        f.write(old[i])
    for i in range(b1, b2):
        f.write(args.input + "\n")
    for i in range(b2, 48):
        f.write(old[i])
else:
    for i in range(0, b2):
        f.write(args.input + "\n")
    for i in range(b2, b1):
        f.write(old[i])
    for i in range(b1, 48):
        f.write(args.input + "\n")
