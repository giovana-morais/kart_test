# -*- coding: utf8 -*-
import pilot as p
import lap as l

class Race:
    def __init__(self, race_data):
        self.data = race_data
        self.podium = []

    def init_race(self):
        pilots = {}
        actual_lap = 1

        for lap_info in self.data:
            pilot_id, pilot_name = lap_info[1], lap_info[2]
            lap_hour, lap_number, lap_time, lap_speed = lap_info[0], lap_info[3], lap_info[4], lap_info[5]

            lap = l.Lap(lap_number, lap_time, lap_speed)

            if pilot_id in pilots:
                pilots[pilot_id].add_lap_info(lap)
            else:
                pilot = p.Pilot(pilot_id, pilot_name)
                pilot.add_lap_info(lap)

                pilots[pilot_id] = pilot

        self.update_podium(pilots)
        self.print_stats(pilots)

        return self.podium
    
    def print_stats(self, pilots):
        print("Final podium:")
        self.print_podium()
        print("Pilots' best laps:")
        self.get_pilots_best_lap(pilots)
        print("Pilot's average speed:")
        self.get_pilots_avgspeed(pilots)


    def get_pilots_best_lap(self, pilots):
        for p in pilots:
            best_lap_number, best_lap_time = pilots[p].get_best_lap()
            print(f"\t{pilots[p].name} best lap was lap {best_lap_number}, which time was {best_lap_time}")
        
    def get_pilots_avgspeed(self, pilots):
        for p in pilots:
            print(f"\t{pilots[p].name} average speed was {round(pilots[p].get_avgspeed(), 3)} km/h")


    def print_podium(self):
        for idx, val in enumerate(self.podium):
            print(f"\t{idx+1} -- ({val.pilot_id}) {val.name} -- Total laps: {val.total_laps}. total time: {val.get_total_race_time()}")

    def update_podium(self, pilots):
        self.podium = sorted([v for k, v in pilots.items()], key=self._get_pilot_sort_key)


    def get_pilots_laps(self, pilots):
        for p in pilots:
            print(f"\t{pilots[p].name} completed {pilots[p].total_laps} laps")

    def get_pilots_laps(self, pilots):
        for p in pilots:
            print(f"\t{pilots[p].name} completed {pilots[p].total_laps} laps")

    def get_partial_podium(self):
        return self.podium

    def _get_pilot_sort_key(self, pilot):
        return pilot.get_total_race_time()


