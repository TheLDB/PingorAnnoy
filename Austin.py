from apscheduler.schedulers.blocking import BlockingScheduler
import os
from playsound import playsound

def ping():
    hostname = "google.com"
    # replace w ip
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        #server is up
        print("1")
    else:
        print("SERVER IS DOWN ALERT ALERT")
        playsound('alarm.mp3')
        ## Choose an mp3 or any sound file to play, accepts web links ( i think)


scheduler = BlockingScheduler()
scheduler.add_job(ping, 'interval', seconds = 5)
scheduler.start()