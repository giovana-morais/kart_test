# -*- coding: utf-8 -*-
import pytest
import datetime
import model.race as r
import model.pilot as p
import model.lap as l
import utils.file_util as fu


def test_podium():
    """
    Podium should be ordered by time
    """
    race_data = "mini_log.txt"

    race = r.Race(fu.parse_file(race_data))
    podium = race.init_race()

    assert podium[0].name == "F.MASSA"
