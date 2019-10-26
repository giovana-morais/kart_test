# -*- coding: utf8 -*-
import pytest
import datetime
import model.pilot as p
import model.lap as l

def test_pilot_creation():
    """
    If all parameters are ok, no error should be raised.
    """
    #lap_info = l.Lap(1, datetime.time(0, 1, 49, 12)
    p.Pilot('011', 'F.MASSA')


def test_pilot_name_type():
    """
    Pilot name should be a string
    """

    with pytest.raises(TypeError):
        p.Pilot('011', 11)

def test_add_wrong_lap_info():
    """
    Each pilot has infos about his/hers laps. It must be a Lap object, otherwise    it should raise a TypeError
    """

    with pytest.raises(TypeError):
        pilot = p.Pilot('011', 'G.MORAIS')
        pilot.add_lap_info(11092)


def test_add_correct_lap_info():
    """
    If all lap infos are fine, our pilot's `lap` list should increase.
    """

    lap_1 = l.Lap(1, datetime.time(0, 1, 49, 209), 44.10)
    lap_2 = l.Lap(2, datetime.time(0, 2, 49, 209), 42.79)

    pilot = p.Pilot('011', 'G.MORAIS')
    pilot.add_lap_info(lap_1)

    assert len(pilot.lap) == 1

    pilot.add_lap_info(lap_2)

    assert len(pilot.lap) == 2


def test_pilots_best_lap():
    """
    Given n laps, pilot.get_best_lap() should return the one finished in less
    time
    """
    lap_1 = l.Lap(1, datetime.time(0, 1, 49, 209), 44.10)
    lap_2 = l.Lap(2, datetime.time(0, 2, 26, 10), 42.79)
    lap_3 = l.Lap(3, datetime.time(0, 1, 20, 959), 47.12)
    lap_4 = l.Lap(4, datetime.time(0, 1, 34, 236), 46.99)

    pilot = p.Pilot('011', 'G.MORAIS')
    pilot.add_lap_info(lap_1)
    pilot.add_lap_info(lap_2)
    pilot.add_lap_info(lap_3)
    pilot.add_lap_info(lap_4)

    best_lap_idx, best_lap_time = pilot.get_best_lap()

    assert best_lap_time == lap_3.time

def test_avg_speed():
    """
    Given n laps, the method should return the correct average speed.
    """

    lap_1 = l.Lap(1, datetime.time(0, 1, 49, 209), 44.10)
    lap_2 = l.Lap(2, datetime.time(0, 2, 26, 10), 42.79)
    lap_3 = l.Lap(3, datetime.time(0, 1, 20, 959), 47.12)
    lap_4 = l.Lap(4, datetime.time(0, 1, 34, 236), 46.99)

    pilot = p.Pilot('011', 'G.MORAIS')
    pilot.add_lap_info(lap_1)
    pilot.add_lap_info(lap_2)
    pilot.add_lap_info(lap_3)
    pilot.add_lap_info(lap_4)

    avg_speed = pilot.get_avg_speed()

    assert avg_speed == 45.25
