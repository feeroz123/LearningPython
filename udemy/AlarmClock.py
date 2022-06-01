# Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

import time
import winsound

alarm_target = 0
print("ALARM CLOCK")

try:
    alarm_target = int(input("\nSet the timer for how many seconds? "))
    print(f"Alarm set for {alarm_target} seconds")
    time.sleep(alarm_target)
    print("Alarm set off !")
    winsound.PlaySound('tada.wav', winsound.SND_FILENAME)
except:
    print("Invalid Input.")




