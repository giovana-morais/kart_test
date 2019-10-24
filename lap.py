# -*- coding: utf8 -*-

class Lap:
    def __init__(self, number, time, speed):
        self.number = number
        self.time = time
        self.speed = speed


    def __repr__(self):
        return {'lap_number': self.number,
                'lap_time': self.time,
                'lap_speed': self.speed}


