import time
import datetime

def set_alarm(alarm_time):
    print(f"alarm set for{alarm_time}")
    sound_file="pythonProject1/alarm mp3.mp3 "
    is_running = True

    while is_running:
        current_time= datetime.date.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time== alarm_time:
            print("Wake Up!😣")

            is_running=False      
if __name__ =="main":
    alarm_time=input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)
   