# Healthy Routine
#Water drinking --->Every 40 min
#Exercise of Eyes --->Every 60min
#Yoga ----> Every 2 hours

from pygame import mixer
from datetime import datetime
from time import time

def MusicOnLoop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("MyLog.txt" , "a") as f:
        f.write(f"{msg} updated at {datetime.now()}\n")

if __name__ == '__main__':
    #MusicOnLoop("file.mp3,"stop")
    init_water = time()
    init_exercise = time()
    init_yoga = time()
    watertime = 7  #--->(For 7sec)
    exercisetime = 10 #--->(For 10sec)
    yogatime = 25 #--->(For 25sec)

    while True:
        if time() - init_water > watertime:
            print("Reminder for DRINKING WATER,Enter 'done' to stop the alarm")
            MusicOnLoop('water.mp3', 'done')
            init_water = time()
            log_now("DRANK WATER AT:")


        if time() - init_exercise > exercisetime:
            print("Reminder for EXERCISE OF EYES,Enter 'done' to stop the alarm")
            MusicOnLoop('clock.mp3', 'done')
            init_exercise = time()
            log_now("DONE EYES EXERCISE AT:")


        if time() - init_yoga > yogatime:
            print("Reminder for DOING YOGA,Enter 'done' to stop the alarm")
            MusicOnLoop('yoga.mp3', 'done')
            init_yoga = time()
            log_now("DRANK YOGA AT:")








