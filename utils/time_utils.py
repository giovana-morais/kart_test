from datetime import timedelta, time

def add_time(time_1, time_2):
    result = timedelta( minutes=time_1.minute, 
                        seconds=time_1.second, 
                        microseconds=time_1.microsecond) + \
            timedelta( minutes=time_2.minute, 
                        seconds=time_2.second, 
                        microseconds=time_2.microsecond) 

    minutes = result.seconds // 60
    hours = minutes // 60
    seconds = result.seconds % 60 

    return time(hours, minutes, seconds, result.microseconds)


