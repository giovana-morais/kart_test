import pilot as p
import lap as l

class Race:
    def __init__(self, race_data):
        self.data = race_data
        self.init_race(self.data)
        self.podium = []

    def init_race(self, race_info):
        pilots = {}
        for lap_info in race_info:
            pilot_id, pilot_name = lap_info[1], lap_info[2]
            lap_hour, lap_number, lap_time, lap_speed = lap_info[0],\
                    lap_info[3],\
                    lap_info[4],\
                    lap_info[5]

            lap = l.Lap(lap_number, lap_time, lap_speed)

            # if lap_number > 1
            if pilot_id in pilots:
                pilots[pilot_id].add_lap_info(lap)
            else:
                pilot = p.Pilot(pilot_id, pilot_name)
                pilot.add_lap_info(lap)

                pilots[pilot_id] = pilot

            print(f"getting {pilot_name} speed at lap {lap_number}")
            print(pilots[pilot_id].get_avgspeed())

    def get_final_podium():
        return "eu que ganhei"

    def get_partial_podium():
        return "eu que tô ganhando"
#        for i in pilots:
#            print(pilots[i].__repr__())




