import time, sys
import os
os.system("cls")

# ANSI коды
PINK = "\033[95m"
RESET = "\033[0m"

time.sleep(29)

lines = [
    ("My girl Liddy used to always smoke", 0.12, 0.4),
    ("Cigarettes when she couldn't sleep", 0.12, 0.10),
    ("She danc disappear for an hour and a half", 0.12, 0.0),
    ("And when she come back she brush her teeth", 0.10, 0.5),
    ("But i could still smell it on her raggedy tee", 0.09, 0.0),
    ("And i could taste it her lips when we kissed", 0.08, 1.70),
    ("Poor little Liddy used to always quit", 0.12, 0.4),
    ("But she never really quit", 0.11, 0.0),
    ("She just say she did", 0.12, 0.4)
]

for line, speed, pause in lines:
    for c in line:
        sys.stdout.write(PINK + c + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print() 
    time.sleep(pause)




