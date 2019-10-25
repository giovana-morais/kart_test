# -*- coding: utf8 -*-

import time, datetime
from utils.time_utils import *

class Pilot:
    def __init__(self, pilot_id, name):
        self.pilot_id = pilot_id
        self.name = name
        self.lap = []
        self.position = 0
        self.total_laps = 0
        self.total_race_time = datetime.time(0, 0, 0, 0)

    def add_lap_info(self, new_lap):
        self.lap.append(new_lap)
        self.total_laps += 1
        self.total_race_time = add_time(self.total_race_time, new_lap.time)

    # update after each lap
    def update_position(self, new_position):
        self.position = new_position

    def __repr__(self):
        return {'pilot_id': self.pilot_id,
                'pilot_name': self.name,
                'pilot_lap': [i.__repr__() for i in self.lap],
                'pilot_position': self.position}

    def get_best_lap(self):
        self.best_lap_number = 1
        self.best_lap_time = self.lap[0].time;

        for idx, val in enumerate(self.lap):
            if val.time < self.best_lap_time:
                self.best_lap_number, self.best_lap_time = idx, val.time

        return self.best_lap_number, self.best_lap_time
        
    def get_total_race_time(self):
        return self.total_race_time

    def get_avgspeed(self):
        self.total_speed = 0
        for l in self.lap:
            self.total_speed += l.speed

        return self.total_speed/self.total_laps
