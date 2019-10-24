class Pilot:
    def __init__(self, pilot_id, name):
        self.pilot_id = pilot_id
        self.name = name
        self.lap = []
        self.position = 0
        self.total_laps = 0
        self.total_race_time = 0

    def add_lap_info(self, new_lap):
        self.lap.append(new_lap)
        self.total_laps += 1

    # update after each lap
    def update_position(self, new_position):
        self.position = new_position

    def get_avgspeed(self):
        self.total_speed = 0
        for i in self.lap:
            self.total_speed += i.speed

        return self.total_speed/self.total_laps

    def get_total_race_time(self):
        return

    def __repr__(self):
        return {'pilot_id': self.pilot_id,
                'pilot_name': self.name,
                'pilot_lap': [i.__repr__() for i in self.lap],
                'pilot_position': self.position}

