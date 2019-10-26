import model.lap as l
import datetime
import pytest

def test_lap_creation():
    """
    With the correct parameters, no error should be raised
    """

    l.Lap(1, datetime.time(0, 1, 0, 0), 40.09)

def test_lap_number_type():
    """
    A lap number should be a int, otherwise a TypeError should be raised
    """

    with pytest.raises(TypeError):
        l.Lap("number", datetime.time(0, 1, 0, 0), 44.4)

def test_lap_time_type():
    """
    A lap time should be a datetime.time, otherwise a TypeError should be raised
    """

    with pytest.raises(TypeError):
        l.Lap(1, "1:11:11", 44.4)

def test_lap_speed_type():
    """
    A lap speed should be a float, otherwise a TypeError should be raised
    """

    with pytest.raises(TypeError):
        l.Lap(1, datetime.time(0, 1, 0, 0), "44.4")

def test_lap_number():
    """
    A lap number can't be 0 or less. If this happens, a ValueError should be
    raised
    """

    with pytest.raises(ValueError):
        l.Lap(-1, datetime.time(0, 1, 0, 0), 44.4)

def test_lap_speed():
    """
    A lap speed can't be 0 or less. If this happens, a ValueError should be
    raised
    """

    with pytest.raises(ValueError):
        l.Lap(1, datetime.time(0, 1, 0, 0), -10.09)


