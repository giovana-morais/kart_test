# -*- coding: utf-8 -*-
import re
import os
import time, datetime
import model.race, model.pilot, model.lap

def parse_file(input_file):
    race_info = []
    if not os.path.isfile(input_file):
        raise Exception("File not found!")

    with open(input_file) as file:
        # skipping first line, since it's just the header of our .csv
        next(file)

        data = file.readlines()

    for l in data:
        race_info.append(parse_line(l))

    return race_info

def parse_line(line):
    full_re = r"(\d{2}:\d{2}:\d{2}.\d{3})\s*(\d{3})\W*(\w.\w*)\s*(\d)\W*(\d:\d\d.\d{3})\s*(\d{2},\d{2,3})"

    match = re.match(full_re, line.strip(' '), re.I)
    hour = match.group(1)
    pilot_id = match.group(2)
    pilot_name = match.group(3)
    lap = match.group(4)
    lap_time = match.group(5)
    speed = match.group(6).replace(",", ".")

    return correct_variable_types(hour, pilot_id, pilot_name, lap, lap_time, speed)

def correct_variable_types(hour, pilot_id, pilot_name, lap_number, lap_time, lap_speed):
    # TODO: usar uma regex aqui tbm pra separar os dados pq fica mais facil
    lap_time = datetime.time(0, 
                            int(lap_time.split(':')[0]), # minute
                            int(lap_time.split(':')[1].split('.')[0]), # seconds
                            int(lap_time.split('.')[1])*1000 # microseconds
                            ) 
    hour = time.strptime(hour, "%H:%M:%S.%f")
    lap_number = int(lap_number)
    lap_speed = float(lap_speed)

    return hour, pilot_id, pilot_name, lap_number, lap_time, lap_speed
