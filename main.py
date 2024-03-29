import utils.file_util as file_util

import sys
import model.race as race, model.pilot as pilor, model.lap as lap

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise FileNotFoundError("Log file missing. Usage: main.py <logfile.txt>")
    else:
        race_info = file_util.parse_file(sys.argv[1])
        r = race.Race(race_info)

        r.init_race()





