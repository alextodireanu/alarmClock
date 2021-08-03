from playsound import playsound
from datetime import datetime


def validate_time(alarm):
    """Method to validate the alarm time"""
    if len(alarm) != 8:
        print("Incorrect time format, please try again...")
        return False
    else:
        try:
            hour = int(alarm[0:2])
            minute = int(alarm[3:5])
            period = alarm[6:]

            if hour < 0 or hour > 12:
                print("Incorrect hour format")
                return False
            elif minute < 0 or minute > 59:
                print("Incorrect minute format")
                return False
            elif period not in ('PM', 'AM'):
                print('Incorrect period format')
                return False

        except ValueError:
            print("Time is not in a valid format, try again")

        else:
            hour = alarm[0:2]
            minute = alarm[3:5]
            print(f'Alarm set for {alarm}')
            if alarm_set(hour, minute, period) is True:
                return True


def alarm_set(alarm_hour, alarm_minute, alarm_period):
    """Method to set the alarm for the given time"""
    while True:
        now = datetime.now()
        # converting the current time to the desired format, 12 hours AM/PM
        current_hour = now.strftime('%I')
        current_minute = now.strftime('%M')
        current_period = now.strftime('%p')

        # comparing the current period, hour and minute with the alarm period, hour and minute
        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_minute == current_minute:
                    print("Alarm ringing")
                    playsound("alarm.wav")
                    return True


while True:
    alarm_time = input("Please enter the time in the following format: HH:MM AM/PM -> ")
    if validate_time(alarm_time.upper()) is True:
        break
