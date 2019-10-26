# -*- coding: utf8 -*-
import datetime

class Lap:
    def __init__(self, number, time, speed):
        self.number = number
        self.time = time
        self.speed = speed

        self.type_check()
        self.is_positive(self.number)
        self.is_positive(self.speed)

    def __repr__(self):
        return {'lap_number': self.number,
                'lap_time': self.time,
                'lap_speed': self.speed}

    def type_check(self):
        self.number_type_check()
        self.time_type_check()
        self.speed_type_check()

    def number_type_check(self):
        if not isinstance(self.number, int):
            raise TypeError(f"Lap number must be an int. Got {type(self.number)} instead.")


    def time_type_check(self):
        if not isinstance(self.time, datetime.time):
            raise TypeError(f"Lap time must be a datetime.time. Got {type(self.time)} instead.")


    def speed_type_check(self):
        if not isinstance(self.speed, float):
            raise TypeError(f"Lap speed must be a float. Got {type(self.speed)} instead.")

    def is_positive(self, x):
        if x <= 0:
            raise ValueError(f"{type(x).__name__} should be greater than 0")

