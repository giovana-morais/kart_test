# -*- coding: utf-8 -*-
import re
import os
import datetime
import race, pilot, lap

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

    return hour, pilot_id, pilot_name, int(lap), lap_time, float(speed)

def correct_variable_types(hour, pilot_id, pilot_name, lap_number, lap_time, lap_speed):
    return

