# -*- coding: utf8 -*-

import model.lap as l
import time, datetime
from utils.time_utils import *

class Pilot:
    def __init__(self, pilot_id, name):
        self.pilot_id = pilot_id
        self.name = name
        self.lap = []
        self.total_laps = 0
        self.total_race_time = datetime.time(0, 0, 0, 0)

        self.type_check()

    def __repr__(self):
        return {'pilot_id': self.pilot_id,
                'pilot_name': self.name,
                'pilot_lap': [i.__repr__() for i in self.lap]}

    def add_lap_info(self, new_lap):
        self.check_lap_info(new_lap)
        self.lap.append(new_lap)
        self.total_laps += 1
        self.total_race_time = add_time(self.total_race_time, new_lap.time)

    def get_best_lap(self):
        self.best_lap_number = 1
        self.best_lap_time = self.lap[0].time;

        for idx, val in enumerate(self.lap):
            if val.time < self.best_lap_time:
                self.best_lap_number, self.best_lap_time = idx, val.time

        return self.best_lap_number, self.best_lap_time

    def get_total_race_time(self):
        return self.total_race_time

    def get_avg_speed(self):
        self.total_speed = 0
        for l in self.lap:
            self.total_speed += l.speed

        return self.total_speed/self.total_laps

    def type_check(self):
        self.name_type_check()

    def name_type_check(self):
        if not isinstance(self.name, str):
            raise TypeError(f"Name must be a str. Got {type(self.name)} instead")
    def check_lap_info(self, lap_info):
        if not isinstance(lap_info, l.Lap):
            raise TypeError(f"Lap info must be a Lap object. Got {type(lap_info)} instead.")
