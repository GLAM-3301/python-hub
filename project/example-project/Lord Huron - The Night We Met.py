import time, sys
import os
os.system("cls")

# ANSI коды
WHITE = "\033[97m"
RESET = "\033[0m"

time.sleep(1)

lines = [
    ("When the night was full of terrors", 0.123, 3),
    ("And your eyes were filled with tears", 0.115, 3),
    ("When you had not touched me yet", 0.131, 3),
    ("Oh, take me back to the night we met", 0.124, 3),
    ("I had all and then most of you", 0.0800, 0),
    ("Some and now none of you", 0.0770, 3),
    ("Take me back to the night we met", 0.136, 3),
    ("I don't know what I'm supposed to do", 0.0750, 0),
    ("Haunted by the ghost of you", 0.0690, 2.5),
    ("Take me back to the night we met.....", 0.130, 0)
]

for line, speed, pause in lines:
    for c in line:
        sys.stdout.write(WHITE + c + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print() 
    time.sleep(pause)