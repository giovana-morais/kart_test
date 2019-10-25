import utils.file_util

import sys
import model.race, model.pilot, model.lap

if __name__ == "__main__":

    if len(sys.argv) < 2:
        # TODO: adicionar tratativa
        # caso o arquivo não esteja nos parâmetros, procurar por algum txt
        # na pasta e perguntar se deve ou não carregá-lo

        raise FileNotFoundError("Log file missing. Usage: main.py <logfile.txt>")
    else:
        race_info = file_util.parse_file(sys.argv[1])
        r = race.Race(race_info)

        r.init_race()





